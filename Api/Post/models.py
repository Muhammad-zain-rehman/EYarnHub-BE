from django.db import models
from main.models import Base
from Api.Company.models import Company
from django.utils.text import slugify

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group


# Create You models here


class Posts(Base):
    """ Post model."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='author_name', null=True, blank=True,)
    content = models.TextField()
    is_active = models.BooleanField(default=True, db_column='IsActive', help_text='I will use this for enable/disable '
                                                                                  'a specific record')

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            self.slug = slugify(self.title)
            super(Posts, self).save()
        except Exception as e:
            raise

        
