"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path    #変更

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hzyhyoka.urls')),                     #追加
    path('', include('accounts.urls')),                     #追加
    path('books/', include('books.urls')),                  #追加(books)
    path('kiki/', include('kiki.urls')),                    # 追加(kiki)
    path('excelupload/', include('excelupload.urls')),      # 追加(excelupload)
    path('exceldownload/', include('exceldownload.urls')),  # 追加(exceldownload)
    path('csvdownload/', include('csvdownload.urls')),      # 追加(exceldownload)
]
