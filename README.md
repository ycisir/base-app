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

#### 4] Apply migrations (optional)
```bash
python manage.py migrate
```

#### 5] Run the development server
```bash
python manage.py runserver
```