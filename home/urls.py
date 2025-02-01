from django.contrib import admin
from django.urls import include, path

from .views import FAQView

urlpatterns = [
    path('faqs/', FAQView.as_view(), name='FAQView'),
]
