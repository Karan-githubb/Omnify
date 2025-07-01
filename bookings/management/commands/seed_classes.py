from django.core.management.base import BaseCommand
from django.utils import timezone
from bookings.models import FitnessClass
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the database with sample fitness classes'

    def handle(self, *args, **options):
        classes = [
            {
                'name': 'Morning Yoga',
                'class_type': 'YOGA',
                'start_time': timezone.now() + timedelta(days=1, hours=8),  # Tomorrow 8 AM
                'end_time': timezone.now() + timedelta(days=1, hours=9),    # Tomorrow 9 AM
                'instructor': 'Jane Smith',
                'capacity': 15,
                'available_slots': 15
            },
            {
                'name': 'Evening Zumba',
                'class_type': 'ZUMBA',
                'start_time': timezone.now() + timedelta(days=1, hours=18),  # Tomorrow 6 PM
                'end_time': timezone.now() + timedelta(days=1, hours=19),    # Tomorrow 7 PM
                'instructor': 'Mike Johnson',
                'capacity': 20,
                'available_slots': 20
            },
            {
                'name': 'HIIT Blast',
                'class_type': 'HIIT',
                'start_time': timezone.now() + timedelta(days=2, hours=10),  # Day after tomorrow 10 AM
                'end_time': timezone.now() + timedelta(days=2, hours=11),    # Day after tomorrow 11 AM
                'instructor': 'Sarah Williams',
                'capacity': 10,
                'available_slots': 10
            }
        ]

        created_count = 0
        for class_data in classes:
            _, created = FitnessClass.objects.get_or_create(
                name=class_data['name'],
                defaults=class_data
            )
            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Successfully seeded {created_count} fitness classes'
        ))