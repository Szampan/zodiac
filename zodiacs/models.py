from django.db import models

class Sign(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # img_url = models.URLField()   

    def __str__(self):
        return self.name

