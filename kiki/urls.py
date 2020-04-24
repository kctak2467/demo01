from django.urls import path
from . import views

urlpatterns = [
    path('', views.KikiList.as_view(), name='kiki'),
    path('<int:pk>/', views.KikiDetail.as_view(), name='detail'),
    path('create/', views.KikiCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.KikiUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.KikiDelete.as_view(), name='delete'),
    path('import/', views.KikiImport.as_view(), name='import'),
    path('export/', views.KikiExport, name='export'),
    path('downloadexcel/', views.KikiDownloadExcel, name='downloadexcel'),
    path('uploadexcel/', views.KikiUploadExcel, name='uploadexcelxx'),
]