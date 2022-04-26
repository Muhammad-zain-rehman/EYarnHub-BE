from django.db import models
from main.models import Base
from django.utils.text import slugify


# Create You models here

class Cargo(Base):
    name = models.CharField(max_length=255, db_column='Name')
    slogan = models.CharField(unique=True, max_length=255, db_column='Slogan')
    phone_number = models.CharField(max_length=255, db_column='Phone_Number')
    is_active = models.BooleanField(default=True, db_column='IsActive', help_text='I will use this for enable/disable '
                                                                                  'a specific record')

    class Meta:
        db_table: 'CargoCompanies'

    def __str__(self):
        return self.name

