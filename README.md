https://docs.djangoproject.com/en/3.0/intro/tutorial01/
https://docs.djangoproject.com/en/3.0/intro/tutorial02/
https://docs.djangoproject.com/en/3.0/intro/tutorial03/

source venv/bin/activate

venv\Scripts\activate

cd python1_django\bank
python manage.py startapp bankapp

after changing models.py:

python manage.py makemigrations bankapp

python manage.py migrate

python manage.py shell

In shell run:

from bankapp.models import Customer, Account
from django.utils import timezone
c1 = Customer(first_name='John', last_name='Smith', birth_date=timezone.now())
c1.save()
c2 = Customer(first_name='Anne', last_name='Brown', birth_date=timezone.now())
c2.save()

exit()

python manage.py createsuperuser



Customer.objects.all()
