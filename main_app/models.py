from django.db import models

# Create your models here.


class Upload_XTF_File_model(models.Model):
    xtf_file = models.FileField(upload_to='media/')
    