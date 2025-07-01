from rest_framework import serializers
from .models import FitnessClass, Booking

class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'class_type', 'start_time', 
                'end_time', 'instructor', 'capacity', 'available_slots']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email']
        extra_kwargs = {
            'fitness_class': {'required': True},
            'client_name': {'required': True},
            'client_email': {'required': True}
        }
        swagger_schema_fields = {
            'example': {
                'fitness_class': 1,
                'client_name': 'John Doe',
                'client_email': 'john@example.com'
            }
        }