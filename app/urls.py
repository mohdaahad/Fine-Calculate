from django.urls import path
from .views import home,chart

urlpatterns = [
    path('', home, name='home'),
    path('chart', chart, name='chart'),
]
