from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        #changes the blog title in the admin area from being called blog 1 and blog 1 to the actual blog title
        return self.summary
