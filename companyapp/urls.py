from django import urls
from django.urls import path

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "companyapp"
from . import views

urlpatterns = [
    path("", views.Table_generation_listview, name="index"),
    path("company/<str:id>", views.CompanyDetailView, name="edit"),
    path("address/<int:pk>", views.Add_address, name="addAddress"),
    path("email/<int:pk>", views.Add_email, name="addemail"),
    path("addnew", views.Addnew_details, name="addnewdetail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
