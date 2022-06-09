from django.db import models
from main.models import Base
from django.utils.text import slugify


# Create You models here

class Company(Base):
    company_name = models.CharField(max_length=255, db_column='Company_Name')
    company_email = models.EmailField(unique=True, max_length=255, db_column='company_email')
    company_manager_name = models.CharField(max_length=255, db_column='Manager_Name')
    company_address = models.CharField(max_length=255, db_column='Company_address')
    about_company = models.TextField()
    company_website = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True, db_column='IsActive', help_text='I will use this for enable/disable '
                                                                                  'a specific record')

    class Meta:
        db_table: 'Company'

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        try:
            if not self.pk:
                self.company_email = self.company_email.replace(" ", "").lower()
            super().save()
        except Exception:
            raise
