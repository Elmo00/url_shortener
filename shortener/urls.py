from django.urls import path

from .views import index, general


app_name = 'shortener'

urlpatterns = [
    path('', index, name='index'),
    path('general/', general, name='general'),
]
