from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.FileField(upload_to = 'documents/')
   class Meta:
      db_table = "profile"