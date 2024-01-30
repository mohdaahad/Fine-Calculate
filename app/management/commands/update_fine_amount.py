# app/management/commands/update_fine_amount.py
from django.core.management.base import BaseCommand
from app.models import UserFine
from django.utils import timezone
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Update fine amount for unpaid fines every minute'

    def handle(self, *args, **options):
        unpaid_fines = UserFine.objects.filter(paid=False, date__lt=timezone.now() - timezone.timedelta(days=1))

        for fine in unpaid_fines:
            days_passed = (timezone.now() - fine.date).days

            if days_passed > 0:
                old_fine_amount = fine.user.fine_amount
                fine.user.fine_amount *= 2 ** days_passed
                new_fine_amount = fine.user.fine_amount
                fine.user.save()

                # Send email notification
                subject = f'Fine Updated ({2 ** days_passed}x Amount)'
                message = f'Your fine amount has been updated from {old_fine_amount} to {new_fine_amount}.'
                send_mail(subject, message, 'from@example.com', [fine.user.email])

        self.stdout.write(self.style.SUCCESS('Successfully updated fine amounts for unpaid fines.'))
