from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from bookings.utils import send_booking_confirmation
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FitnessClassListView(APIView):
    @swagger_auto_schema(
        responses={200: FitnessClassSerializer(many=True)},
        operation_description="List all upcoming fitness classes",
        tags=['Classes']
    )
    def get(self, request):
        classes = FitnessClass.objects.filter(start_time__gte=timezone.now())
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class CreateBookingView(APIView):
    @swagger_auto_schema(
        request_body=BookingSerializer,
        responses={
            201: BookingSerializer,
            400: "Invalid input/No slots available"
        },
        operation_description="Book a fitness class slot",
        tags=['Bookings']
    )
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            fitness_class = serializer.validated_data['fitness_class']
            
            if fitness_class.available_slots <= 0:
                return Response(
                    {"error": "No available slots for this class"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            fitness_class.available_slots -= 1
            fitness_class.save()
            booking = serializer.save()

            # Send confirmation email
            try:
                send_booking_confirmation(booking)
            except Exception as e:
                print(f"Failed to send email: {e}")
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientBookingsView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'email',
                openapi.IN_QUERY,
                description="Filter bookings by client email",
                type=openapi.TYPE_STRING,
                required=True
            )
        ],
        tags=['Bookings']
    )
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response(
                {"error": "Email parameter is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)