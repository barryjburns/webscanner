from django.contrib import admin
from scanner.models import Scan, Plugin, ScanPlugin

for model in Scan, Plugin, ScanPlugin:
  admin.site.register(model)
