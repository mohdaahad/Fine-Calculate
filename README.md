git clone https://github.com/mohdaahad/Fine-Calculate.git

cd Fine-Calculate

# Create initial migrations
python manage.py makemigrations

# Apply migrations to the database
python manage.py migrate


python manage.py createsuperuser


python manage.py runserver


python manage.py update_fine_amount
