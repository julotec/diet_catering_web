from django.db import models
from django.utils import timezone

# Create your models here.


class Order_Diet(models.Model):
    VARIANTS_CHOICES = [
        ('option1', 'Allday'),
        ('option2', 'Family pack'),
        ('option3', 'Medium'),
        ('option4', 'Lunch'),
        ('option5', 'Lunch+'),
        ('option6', 'Medium+'),
    ]
    KCAL_CHOICES = [
        ('option1', '1200 kcal'),
        ('option2', '1400 kcal'),
        ('option3', '1500 kcal'),
        ('option4', '1750 kcal'),
        ('option5', '1900 kcal'),
        ('option6', '2150 kcal'),
        ('option7', '2350 kcal'),
        ('option8', '2550 kcal'),
        ('option9', '2700 kcal'),
    ]

    Name = models.CharField(max_length=55)
    Number = models.IntegerField(max_length = 55)
    Email = models.EmailField(max_length=55)
    Variant = models.CharField(max_length=55, choices=VARIANTS_CHOICES, default='option1')
    Kcal = models.CharField(max_length=55, choices=KCAL_CHOICES, default= 'option1')
    Date = models.DateField(default = timezone.now)
    

    
