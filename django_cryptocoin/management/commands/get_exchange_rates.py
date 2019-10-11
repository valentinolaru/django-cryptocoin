import requests

from django.core.management.base import BaseCommand
from django_cryptocoin.models import ExchangeRate
from django_cryptocoin import settings


class Command(BaseCommand):
    args = ''
    help = 'Executes parsing exchange rates from btc-e.com'

    def handle(self, *args, **options):
        session = requests.Session()
        session.get('https://api.cryptonator.com/api/ticker/btc-eur/')

        for pair in settings.CURRENCY_PAIRS:
            currencies = pair.split('_')
            updated_pair = '-'.join(pair.split('_'))
            try:
                conn = session.get('https://api.cryptonator.com/api/ticker/%s/' % updated_pair)
                response = conn.json()
            except Exception as e:
                self.stdout.write('Get error: {}'.format(e))
                response = None

            print(response)
            if response:
                if response.get('error'):
                    self.stdout.write(response['error'])
                    continue
                print(currencies)
                rate, created = ExchangeRate.objects.get_or_create(currency1=currencies[0], currency2=currencies[1])
                rate.rate = float(response['ticker']['price'])
                rate.save()
                self.stdout.write('Successfully updated')
            else:
                self.stdout.write('Error!')

        self.stdout.write('Successfully executed')
