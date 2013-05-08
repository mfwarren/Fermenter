
from main.models import Brew, TemperatureData
from main.views import get_current_brew
from main.rpi_control import *

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

log = get_task_logger(__name__)


@periodic_task(run_every=crontab(minute='*'))
def check_temperature():

    current_brew = get_current_brew()

    if current_brew:
        measured_temperature = read_current_temperature()
        if measured_temperature > current_burew.target_temperature + 0.5:
            turn_on_cooling()
        if measured_temperature < current_brew.target_temperature - 0.5:
            turn_off_cooling()

        #record temperature
        TemperatureData(temperature=measured_temperature,
                target=current_brew.target_temperature,
                brew=current_brew).save()

