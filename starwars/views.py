import datetime
import os
import requests
import petl as etl
import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files import File
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import DatasetMetadata, Character


# Define the base URL for the SWAPI API
SWAPI_BASE_URL = 'https://swapi.dev/api'


@require_http_methods(['GET'])
def collections_list(request):
    # Fetch the list of downloaded datasets
    datasets = DatasetMetadata.objects.all()
    # Render the index template with the datasets list    
    return render(request, 'starwars/collections_list.html', {'datasets': datasets})


@require_http_methods(['POST'])
@csrf_exempt
def download_data(request):
    # Define the URL to fetch data from
    data_url = f'{SWAPI_BASE_URL}/people/'
    
    # Use a generator function to fetch all pages of data
    def fetch_all_data():
        nonlocal data_url
        while data_url is not None:
            response = requests.get(data_url)
            data = response.json()
            data_url = data['next']
            yield from data['results']

    # Fetch all pages of data and transform it into a list of dicts
    data = list(fetch_all_data())
    transformed_data = []
    for d in data:
        # Use the homeworld URL to get the planet name
        planet_response = requests.get(d['homeworld'])
        planet_data = planet_response.json()
        homeworld_name = planet_data['name']
        edited_date_str = planet_data['edited']

        # Convert edited_date_str to datetime object and format as string
        edited_date = datetime.datetime.strptime(edited_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        edited_date_str_formatted = edited_date.strftime('%Y-%m-%d')

        # Add the row with the resolved homeworld name
        transformed_data.append({
            'name': d['name'],
            'height': d['height'],
            'mass': d['mass'],
            'eye_color': d['eye_color'],
            'hair_color': d['hair_color'],
            'skin_color': d['skin_color'],
            'birth_year': d['birth_year'],
            'gender': d['gender'],
            'homeworld': homeworld_name,
            'date': edited_date_str_formatted,
        })
    
    # Convert the transformed data to a PETL table and write it to a CSV file
    table = etl.fromdicts(transformed_data)
    filename = f'swapi_people_{datetime.datetime.now():%Y-%m-%d_%H-%M-%S}.csv'
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    etl.tocsv(table, file_path)
    
    # Save metadata for the downloaded file in the database
    metadata = DatasetMetadata(filename=filename, date=datetime.datetime.now(), dataset_file=file_path)
    metadata.save()

    # Save the contents of the CSV file to the CharacterInline
    table = etl.fromcsv(file_path)
    for row in etl.dicts(table):
        character = Character(
            dataset=metadata,
            name=row['name'],
            height=row['height'],
            mass=row['mass'],
            eye_color=row['eye_color'],
            hair_color=row['hair_color'],
            skin_color=row['skin_color'],
            birth_year=row['birth_year'],
            gender=row['gender'],
            homeworld=row['homeworld'],
            date=row['date'],
        )
        character.save()

    # Return the CSV file as a response to the user
    response = HttpResponse(open(file_path, 'rb').read(), content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return redirect('starwars:collections_list')


def collections_detail(request, dataset_id):
    dataset = DatasetMetadata.objects.get(pk=dataset_id)
    character_list = dataset.character_set.all()
    paginator = Paginator(character_list, 10)  # Show 10 results per page

    page = request.GET.get('page')
    try:
        characters = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        characters = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        characters = paginator.page(paginator.num_pages)

    context = {'characters': characters, 'dataset': dataset}
    return render(request, 'starwars/collections_detail.html', context)