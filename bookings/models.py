from django.db import models
from django.utils import timezone

class FitnessClass(models.Model):
    CLASS_TYPES = [
        ('YOGA', 'Yoga'),
        ('ZUMBA', 'Zumba'),
        ('HIIT', 'HIIT'),
    ]
    
    name = models.CharField(max_length=100)
    class_type = models.CharField(max_length=10, choices=CLASS_TYPES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.get_class_type_display()})"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.fitness_class.name}"