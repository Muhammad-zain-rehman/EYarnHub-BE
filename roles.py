import os
import django

from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EyarnHub.settings')
django.setup()

from Api.Users.models import User, Role, AccessLevel


def add_roles():
    total_roles = AccessLevel.DICT
    print(total_roles)
    obj = ''
    for acl, role in total_roles.items():  # acl stands for access level
        role_object = Role.objects.filter(name=role, access_level=acl)
        if role_object.exists():
            print(f'{role}is exists')
            continue
        else:
            new_role_object = Role(name=role, access_level=acl)
            new_role_object.save()
            obj = True
            print(f'{role} newly added')
    if obj:
        print("All above Role has been Added successfully")


if __name__ == "__main__":
    add_roles()
