from django.urls import path
from . import views

app_name = 'exceldownload'
urlpatterns = [
    path('', views.index, name='index'),   # 一覧
]