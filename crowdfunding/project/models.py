from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    #owner = models.CharField(max_length=200)
    owner = models.ForeignKey(
    get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    CATEGORY_CHOICES = (
    ('Vegetarian', 'Veg'),
    ('Non-Vegetarian','Non-Veg')
    )
    foodtypes = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )

        
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
)


    