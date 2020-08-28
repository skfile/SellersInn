from django.core.management.base import BaseCommand
from main.admin import *
from main.models import *


class Command(BaseCommand):
    # help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):

        userForm.objects.all().delete()
        newsletter.objects.all().delete()
