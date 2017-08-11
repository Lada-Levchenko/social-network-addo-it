from django.core.management import BaseCommand
from users.models import User
from social_network_project.local_settings import ADMIN_EMAIL, ADMIN_PASSWORD


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(email=ADMIN_EMAIL, password=ADMIN_PASSWORD)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Users exist')
