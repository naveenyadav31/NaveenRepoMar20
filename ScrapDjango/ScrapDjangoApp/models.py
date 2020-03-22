from django.db import models


class CompanyDetails(models.Model):

    Business_Name = models.TextField()
    Website = models.TextField()
    Category = models.TextField()
    City = models.TextField()