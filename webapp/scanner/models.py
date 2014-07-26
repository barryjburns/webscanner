from django.db import models
import uuid

# Create your models here.

new_guid = lambda: str(uuid.uuid4())
GuidField = lambda: models.CharField(max_length = 36, null = False, blank = False, default = new_guid, unique = True, db_index = True, editable = False)

class Scan(models.Model):
  guid = GuidField()
  user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
  created = models.DateTimeField(auto_now_add = True, null = False)
  started = models.DateTimeField(null = True, default = None)
  finished = models.DateTimeField(null = True, default = None)
  host = models.CharField(max_length = 255, null = False, blank = False)
  plugins = models.ManyToManyField('Plugin', related_name = 'scans', through = 'ScanPlugin')

class Plugin(models.Model):
  guid = GuidField()
  name = models.CharField(max_length = 255, null = False, blank = False, unique = True, db_index = True)

class ScanPlugin(models.Model):
  guid = GuidField()
  scan = models.ForeignKey('Scan', on_delete = models.CASCADE)
  plugin = models.ForeignKey('Plugin', on_delete = models.CASCADE)
  created = models.DateTimeField(auto_now_add = True, null = False)
  started = models.DateTimeField(null = True, default = None)
  finished = models.DateTimeField(null = True, default = None)
  result = models.TextField(null = True, blank = True, default = None)
