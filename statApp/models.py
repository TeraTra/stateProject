from django.db import models


#choice for stat
STAT = (
    ('Modelisation', 'Modelisation'),
    ('Design', 'Design'),
    ('Conception', 'Conception'),
    ('Deployement', 'Deployement'),
    ('Fin', 'Fin')
)

# Create your models here.
class Project(models.Model):
    nameProject = models.CharField(max_length=50)
    projectProgress = models.CharField(max_length=50, choices=STAT, verbose_name='stat')
    link_site = models.URLField(max_length=255)

