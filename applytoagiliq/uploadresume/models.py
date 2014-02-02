from django.db import models
from applytoagiliq import settings

# Create your models here.

class Resume(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    project_url = models.URLField(max_length=150)
    code_url = models.URLField(max_length=150)
    resume = models.FileField(upload_to=settings.MEDIA_ROOT)
    
    def __unicode__(self):
        return "Name: %s %s" % (self.first_name, self.last_name)
    

