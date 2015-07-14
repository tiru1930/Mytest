from django.db import models
from time import time

# Create your models here.

def get_upload_file_name(instance, filename):
    return 'UPLOAD_FILE_PATTERN' % (str(time()).replace('.','_'), filename)

class Article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField('date published')
    likes=models.IntegerField(default=0)
    #thumbnail = models.FileField(upload_to=get_upload_file_name)

    def __unicode__(self):
        return self.title
