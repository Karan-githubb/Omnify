from django.urls import path
from .views import (
    FitnessClassListView,
    CreateBookingView,
    ClientBookingsView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Fitness Studio API",
        default_version='v1',
        description="Booking system for fitness classes",
    ),
    public=True,
)


urlpatterns = [
    path('classes/', FitnessClassListView.as_view(), name='class-list'),
    path('book/', CreateBookingView.as_view(), name='create-booking'),
    path('bookings/', ClientBookingsView.as_view(), name='client-bookings'),
    
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]