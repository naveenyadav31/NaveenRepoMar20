from django.views.generic import ListView
from ScrapDjangoApp.models import CompanyDetails


class CompanyDetailsList(ListView):
    model = CompanyDetails
    template_name = 'ScrapDjangoApp/list.html'
    context_object_name = 'company_details'
