from django.db import models

class HealthCenter(models.Model):
    """
        Information about location and health centers available
    """
    name = models.CharField(max_length=100)
    district_of_health_center = models.CharField(max_length=100)
    village_of_health_center = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
    
class HealthWorker(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    health_center_affiliation = models.ManyToManyField(HealthCenter)
    