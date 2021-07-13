# Paybok

## Steps to start

create virtual evnvironment 
    python -m pip install virtualenv

    virtualenv venv
    
    for Windows : venv\Scripts\activate
    for Mac : Source vevn/bin/activate
    
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
