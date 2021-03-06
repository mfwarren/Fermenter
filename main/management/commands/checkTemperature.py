from django.core.management.base import BaseCommand, CommandError

from main.models import Brew, TemperatureData
from main.views import get_current_brew
from main.rpi_control import *


class Command(BaseCommand):
    help = 'Checks the temperature and controls the fans'

    def handle(self, *args, **options):
        current_brew = get_current_brew()

        if current_brew:
            measured_temperature = read_current_temperature()[0]
            if measured_temperature > current_brew.target_temperature + 0.5:
                turn_on_cooling()
            if measured_temperature < current_brew.target_temperature - 0.5:
                turn_off_cooling()

            #record temperature
            print measured_temperature
            TemperatureData(temperature=measured_temperature,
                    target=current_brew.target_temperature,
                    brew=current_brew).save()


