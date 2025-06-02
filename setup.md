# base app
my django webapp structure

#### 1] Clone the Repository
```bash
git clone https://github.com/ycisir/base-app.git
```

#### 2] Create your project folder activate a venv
```bash
mkdir new_project
cd new_project
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install django python-decouple
```

#### 3] Create django project using template
```bash
django-admin startproject webapp . --template=/home/yasir/Documents/django/base-app
pip freeze > requirements.txt
```

#### 4] Generate secret key and create .env file at /project-name/webapp/.env

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

- Paste generated secret key in .env
```bash
ENVIRONMENT=DEVELOPMENT
SECRET_KEY=paste here
```

#### 5] Migrate and run the development server
```bash
python manage.py migrate
python manage.py runserver
```
