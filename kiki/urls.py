from django.urls import path
from . import views

urlpatterns = [
    path('', views.KikiList.as_view(), name='kiki'),
    path('<int:pk>/', views.KikiDetail.as_view(), name='detail'),
    path('create/', views.KikiCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.KikiUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.KikiDelete.as_view(), name='delete'),
]