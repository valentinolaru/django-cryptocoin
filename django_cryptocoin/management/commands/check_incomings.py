from datetime import timedelta
from django.core.management.base import BaseCommand
from django.db.models import Q, F
from django.utils import timezone
from django_cryptocoin.bitcoinrpc.authproxy import AuthServiceProxy
from django_cryptocoin.models import CryptoOrder
from django_cryptocoin import settings
from django_cryptocoin.signals import after_pay_confirmation


class Command(BaseCommand):
    args = ''
    help = 'check incomings for open invoices'

    def handle(self, *args, **options):

        orders = CryptoOrder.objects.filter(
            Q(date__gte=timezone.now()-timedelta(seconds=settings.INVOICE_TIME)) |
            Q(amount_received_confirmed__lt=F('amount_received'))
        )
        for order in orders:
            if order.currency not in settings.CONNECTION_STRING:
                continue
            try:
                access = AuthServiceProxy(settings.CONNECTION_STRING[order.currency])
                received = access.getreceivedbyaddress(order.addr, 0)
                received_confirmed = access.getreceivedbyaddress(order.addr, settings.CONFIRMATIONS[order.currency])

                if received != order.amount_received or received_confirmed != order.amount_received_confirmed:
                    order.amount_received = received
                    order.amount_received_confirmed = received_confirmed
                    order.save()

                if not order.processed and order.amount_received_confirmed >= order.amount:
                    after_pay_confirmation.send(sender=order)
                    order.processed = True
                    order.save()

            except Exception as e:
                continue

        self.stdout.write('Successfully executed')
