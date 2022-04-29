import os
import django

from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EyarnHub.settings')
django.setup()

from django.conf import settings
from django.core.management import BaseCommand
from Api.Users.models import User, Role


def superUser():
    try:
        name = "Super Admin"
        email = settings.SUPER_USER or "superuser@yopamil.com"
        is_staff = True
        is_active = True
        user_role = "super_admin"
        password = "Pass1234@"
        is_superuser = True
        user_obj = {"name": name,
                    "email": email,
                    "is_active": is_active,
                    'user_role': Role.objects.get(code=user_role),
                    "is_superuser": is_superuser
                    }
        try:
            user = User.objects.create(**user_obj)
            user.set_password(password)
            user.save()
            print(f'Email: {email}')
            print(f'Password: {password}')
            print("User is created")
        except Exception as e:
            print(f"User is not created: {e}")

    except Exception as e:
        print(e)
        print(f"User is not created exception:{e}")


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            superUser()
        except Exception as e:
            print(e)
