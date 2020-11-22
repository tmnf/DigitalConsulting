@Echo off

python manage.py makemigrations DigitalPlatform
python manage.py sqlmigrate DigitalPlatform 0001
python manage.py migrate