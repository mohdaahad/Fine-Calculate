from django.contrib import admin
from .models import FineChart, UserFine, User,BankMony

admin.site.register(User)
admin.site.register(FineChart)
admin.site.register(UserFine)
admin.site.register(BankMony)