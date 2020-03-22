from django.urls import path, include
from ScrapDjangoApp.views import CompanyDetailsList

urlpatterns = [
    path('', CompanyDetailsList.as_view(), name='CompanyDetails-list')
]