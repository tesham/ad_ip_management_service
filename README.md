## Django REST API for User Authentication with PostgreSQL
This project implements a RESTful API using Django and Django REST Framework (DRF) for user IP management.
The API includes IP fetch, create, update request.
It produces ip task's audit log and send it to audit consumer

## Features

- IP view
- IP create with label
- Update label of IP
- Produce RabbitMQ audit log
- PostgreSQL as the database backend

### Prerequisites

- Python 3.9
- PostgreSQL
- Django 4.1.0
- Django REST Framework 3.14

### Installation

1. clone the repository

2. Create and activate a virtual environment if it doesn't exist in the project folder:
```
    python -m venv venv
    source venv/bin/activate
```

3. Install all the requirements using `pip`:
```
    pip install -r requirements.txt
```

4. Add database connection information in main `settings.py` 
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
```

5. Apply migrations from terminal
```
    python manage.py makemigrations ip_management
    python manage.py migrate ip_management
    
    model structure:
    class IP(models.Model):
        id = [primary key, auto generated]
        ip = models.CharField(max_length=100, unique=True)
        create_time = models.DateTimeField(auto_now_add=True)
        update_time = models.DateTimeField(null=True, blank=True)
        label = models.CharField(max_length=500, blank=True, null=True)
        created_by = models.CharField(max_length=250, blank=True, null=True)
```

6. Put RabbitMQ config in setting.py

```
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'rabbitmq')
    RABBITMQ_PORT = 5672
    RABBITMQ_USER = 'guest'
    RABBITMQ_PASSWORD = 'guest'
```
    
7. Start the server:
```
    python manage.py runserver
```


### Configuration

Update the `settings.py` file with your configurations. Ensure you have the `SECRET_KEY`, `JWT_SECRET_KEY` and other necessary configurations set.

### Entry point

ip_service/urls