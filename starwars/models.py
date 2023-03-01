from django.db import models


class DatasetMetadata(models.Model):
    filename = models.CharField(max_length=255)
    date = models.DateTimeField()
    dataset_file = models.FileField(upload_to='')

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ('-date',)
        get_latest_by = ('-date',)
        verbose_name = 'Dataset'
        verbose_name_plural = 'Datasets'


class Character(models.Model):
    dataset = models.ForeignKey('DatasetMetadata', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    mass = models.CharField(max_length=255)
    eye_color = models.CharField(max_length=255)
    hair_color = models.CharField(max_length=255)
    skin_color = models.CharField(max_length=255)
    birth_year = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    homeworld = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        get_latest_by = ('name',)
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'