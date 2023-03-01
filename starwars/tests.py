from django.test import TestCase
from django.urls import reverse

from .models import DatasetMetadata


class StarWarsAPITestCase(TestCase):
    def test_download_data_view(self):
        """
        Test that the download_data view downloads the data and saves the metadata
        """
        response = self.client.post(reverse('starwars:download_data'))
        self.assertEqual(response.status_code, 200)

        # Check that the file was created and has some content
        dataset_file = response.streaming_content.__next__()
        self.assertTrue(dataset_file)
        
        # Check that metadata was saved
        metadata = DatasetMetadata.objects.first()
        self.assertEqual(metadata.filename, 'starwars_dataset.csv')

    def test_index_view(self):
        """
        Test that the index view displays the button to download the data
        """
        response = self.client.get(reverse('starwars:index'))
        self.assertContains(response, 'Download data')
