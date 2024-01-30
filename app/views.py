from django.shortcuts import render, reverse
from .models import User,BankMony,FineChart

def home(request):
    users = User.objects.all()
    bank_mony = BankMony.objects.first()
    context = {'users': users, 'bank_mony': bank_mony} 
    return render(request, 'app/home.html',context)

def chart(request):
    fines = FineChart.objects.all()
    bank_mony = BankMony.objects.first()   
    return render(request, 'app/fine_chart.html',{'fines': fines,'bank_mony': bank_mony})