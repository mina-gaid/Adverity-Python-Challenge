from django.contrib import admin

from .models import DatasetMetadata, Character


class CharacterInline(admin.TabularInline):
    model = Character
    list_display = ('name', 'homeworld', 'gender',)
    list_filter = ('birth_year', 'gender',)
    search_fields = ('name', 'homeworld',)


@admin.register(DatasetMetadata)
class DatasetMetadataAdmin(admin.ModelAdmin):
    inlines = [CharacterInline,]
    list_display = ('filename', 'date', 'dataset_file',)
    list_filter = ('date',)
    search_fields = ('filename',)


admin.site.site_header = 'Star Wars Admin'
admin.site.index_title = 'Star Wars API'
