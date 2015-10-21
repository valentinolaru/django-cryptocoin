import requests

from django.core.management.base import BaseCommand
from django_cryptocoin.models import ExchangeRate
from django_cryptocoin import settings


class Command(BaseCommand):
    args = ''
    help = 'Executes parsing exchange rates from btc-e.com'

    def handle(self, *args, **options):

        for pair in settings.CURRENCY_PAIRS:
            currencies = pair.split('_')
            try:
                response = requests.get('http://btc-e.com/api/2/{}/ticker'.format(pair)).json()
            except Exception as e:
                self.stdout.write('Get error: {}'.format(e))
                response = None

            if response:
                rate, created = ExchangeRate.objects.get_or_create(currency1=currencies[0], currency2=currencies[1])
                rate.rate = response['ticker']['last']
                rate.save()

        self.stdout.write('Successfully executed')
