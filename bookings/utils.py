# bookings/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_booking_confirmation(booking):
    subject = f"Booking Confirmation for {booking.fitness_class.name}"
    message = f"""
    Hello {booking.client_name},
    
    Your booking for {booking.fitness_class.name} with {booking.fitness_class.instructor}
    on {booking.fitness_class.start_time.strftime('%A, %B %d at %I:%M %p')} is confirmed.
    
    Thank you!
    {settings.SITE_NAME}
    """
    send_mail(
        subject,
        message.strip(),
        settings.DEFAULT_FROM_EMAIL,
        [booking.client_email],
        fail_silently=False,
    )