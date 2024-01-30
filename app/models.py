from django.db import models
from django.utils import timezone
from django.core.mail import send_mail

class User(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    fine_amount = models.IntegerField() 

    def __str__(self):
        return self.user_name

class FineChart(models.Model):
    fine_name = models.CharField(max_length=255)
    fine_amount = models.IntegerField() 

    def __str__(self):
        return self.fine_name

class BankMony(models.Model):
    total_mony = models.IntegerField() 

    def __str__(self):
        return f"Total Money: {self.total_mony}"

class UserFine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fine_chart = models.ForeignKey(FineChart, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.user_name} - {self.fine_chart.fine_name}"

    def send_notification_email(self, subject, message):
        send_mail(subject, message, 'qadeeba123@gmail.com', [self.user.email])

    def save(self, *args, **kwargs):
        if self.paid:
            # Calculate days_passed to determine the multiplier for fine amount
            days_passed = (timezone.now() - self.date).days
            multiplier = 2 ** days_passed if days_passed > 0 else 1

            # Update user's fine_amount based on the multiplier
            self.user.fine_amount -= self.fine_chart.fine_amount * multiplier
            total_mony_change = self.fine_chart.fine_amount * multiplier

            # Send email notification for paid fine
            subject = f'Fine Paid ({multiplier}x Amount)'
            message = f'Your fine for {self.fine_chart.fine_name} of {self.fine_chart.fine_amount} has been paid. The {multiplier}x amount has been deducted.'
            self.send_notification_email(subject, message)

            # Update user's total fine amount and bank's total money
            self.user.save()
            bank_mony, _ = BankMony.objects.get_or_create(pk=1)
            bank_mony.total_mony += total_mony_change
            bank_mony.save()

        else:
            # If the fine is not paid, update user's fine_amount when UserFine is created
            self.user.fine_amount += self.fine_chart.fine_amount
            self.user.save()

            # Send email notification for unpaid fine
            subject = 'Fine Reminder'
            message = f'Your fine for {self.fine_chart.fine_name} of {self.fine_chart.fine_amount} is still pending. Please make the payment.'
            self.send_notification_email(subject, message)

        super().save(*args, **kwargs)

