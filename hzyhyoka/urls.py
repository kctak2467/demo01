from django.urls import path

from . import views

app_name = 'hzyhyoka'
urlpatterns = [
    path('', views.top, name='top'),
]