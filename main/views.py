# Create your views here.
import datetime

from main.models import *
from main.forms import *

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def get_current_brew():

    current_brew = list(Brew.objects.filter(complete_date__isnull=True)[:1])

    if current_brew:
        return current_brew[0]
    return None


def dashboard(request, template='dashboard.html', section='dashboard'):
    today = datetime.date.today()
    week_ago = datetime.datetime.now() + datetime.timedelta(days=-7)

    current_brew = list(Brew.objects.filter(complete_date__isnull=True)[:1])

    if current_brew:
        current_brew = current_brew[0]
        data = TemperatureData.objects.filter(date__gte=week_ago, brew=current_brew)
    else:
        brew_form = BrewForm()

    return render_to_response(template, locals(),context_instance=RequestContext(request))

def start_brew(request):
    if request.method == 'POST':
        brew_form = BrewForm(request.POST)
        if brew_form.is_valid():
            brew = brew_form.save()
            return redirect(reverse('dashboard'))

def finish_brew(request):
    if request.method == 'POST':

        current_brew = get_current_brew()

        if current_brew:
            current_brew.complete_date = datetime.datetime.now()
            current_brew.save()
            return redirect(reverse('dashboard'))

