import string
import json
import django.db.utils
from django.core.management.base import BaseCommand, CommandError
from bugdemo.models import SideA, SideB


def create_side_a(name):
    sda = SideA(name=name)
    sda.save()
    sda.populate_sideb_links()



class Command(BaseCommand):
    help = 'adds backhoes from a scrape into the db'


    def handle(self, *args, **options):

        SideB(name="Tom").save()
        SideB(name="Dick").save()
        SideB(name="Harry").save()

        create_side_a("Red")
        create_side_a("green")
        create_side_a("blue")
