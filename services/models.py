from django.db import models
from accounts.models import UserAccount


# Create your models here.
class CaService(models.Model):
    class SaveType(models.TextChoices):
        DRAFT = 'Draft'
        SAVED = 'Saved'
        PUBLISH = 'Publish'

    ca_id = models.CharField(max_length=63)
    short_title = models.CharField(max_length=63)
    subtitle = models.CharField(max_length=255)
    intro_photo = models.ImageField(upload_to='intro_photo/%Y/%m/%d')
    price = models.IntegerField()
    intro_video = models.FileField(upload_to='intro_video/%Y/%m/%d')
    title = models.CharField(max_length=127)
    service_required_for = models.CharField(max_length=127)
    description_main = models.CharField(max_length=511)
    description_1 = models.CharField(max_length=63)
    description_2 = models.CharField(max_length=63)
    description_3 = models.CharField(max_length=63)
    description_4 = models.CharField(max_length=63)
    description_5 = models.CharField(max_length=63)
    description_6 = models.CharField(max_length=63)
    description_7 = models.CharField(max_length=63)
    description_8 = models.CharField(max_length=63)
    service_include_1 = models.CharField(max_length=127)
    service_include_2 = models.CharField(max_length=127)
    service_include_3 = models.CharField(max_length=127)
    service_include_4 = models.CharField(max_length=127)
    service_include_5 = models.CharField(max_length=127)
    service_include_6 = models.CharField(max_length=127)
    service_include_7 = models.CharField(max_length=127)
    service_include_8 = models.CharField(max_length=127)
    document_required_1 = models.CharField(max_length=127)
    document_required_2 = models.CharField(max_length=127)
    document_required_3 = models.CharField(max_length=127)
    document_required_4 = models.CharField(max_length=127)
    document_required_5 = models.CharField(max_length=127)
    document_required_6 = models.CharField(max_length=127)
    document_required_7 = models.CharField(max_length=127)
    document_required_8 = models.CharField(max_length=127)
    document_required_9 = models.CharField(max_length=127)
    total_duration = models.DurationField()
    steps_1 = models.CharField(max_length=127)
    steps_2 = models.CharField(max_length=127)
    steps_3 = models.CharField(max_length=127)
    steps_4 = models.CharField(max_length=127)
    steps_5 = models.CharField(max_length=127)
    steps_6 = models.CharField(max_length=127)
    steps_7 = models.CharField(max_length=127)
    steps_8 = models.CharField(max_length=127)
    steps_9 = models.CharField(max_length=127)
    saved_as = models.CharField(max_length=31, choices=SaveType.choices, default=SaveType.DRAFT)
    star_rating = models.DecimalField(decimal_places=1, max_digits=4)

    def __str__(self):
        return self.ca_id + " -- " + self.title

    class Meta:
        ordering = ['-id']
