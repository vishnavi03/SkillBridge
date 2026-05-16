from django.contrib import admin
from .models import ServiceRequest, Review

admin.site.register(ServiceRequest)
admin.site.register(Review)