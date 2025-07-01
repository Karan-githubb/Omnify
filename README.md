# Fitness Studio Booking API

A Django REST framework API for managing fitness class bookings with Swagger/OpenAPI documentation.

## Features

- Class listing with available slots  
- Booking management  
- Client booking history  
- Interactive API documentation  
- Timezone-aware scheduling  

## Setup

### Prerequisites
- Python 3.8+  
- Django 3.2+  
- SQLite (included) or PostgreSQL  

### Installation

1. Clone the repository:
   git clone https://github.com/Karan-githubb/Omnify.git
   cd Omnify

2. Create and activate virtual environment:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Create admin user:
   python manage.py createsuperuser

6. Seed sample data:
   python manage.py seed_classes


### Running the Server
python manage.py runserver


## API Documentation

Access interactive documentation at:

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)  
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)  


## Endpoints

| Endpoint         | Method | Description                    |
|------------------|--------|--------------------------------|
| `/classes/`      | GET    | List all upcoming classes      |
| `/book/`         | POST   | Create a new booking           |
| `/bookings/`     | GET    | Get bookings by client email   |

