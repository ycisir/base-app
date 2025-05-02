# django-app
django app structure for webapp

#### Prerequisites
- python 3.12
- git (recommended)
- venv (recommended)

#### 1] Clone the Repository
```bash
git clone https://github.com/ycisir/django-app.git
cd django-app
```

#### 2] Create and Activate a Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

#### 3] Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4] Create .env file at /django-app/webapp/.env and paste these two lines

```bash
ENVIRONMENT=DEVELOPMENT
SECRET_KEY=django-insecure-yxjo-g8^%v75yj(+=p#9n*jy9)m+pizp)w)n&+1j&q%-+h3j(t
```

#### 5] Migrate and run the development server
```bash
python manage.py migrate
python manage.py runserver
```
