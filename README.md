# base app

- clone the repo
- create project folder and activate venv
- install these
  ```bash
  pip install django python-decouple
  ```
- create django project using template
  ```bash
  django-admin startproject webapp . --template=/home/yasir/Documents/django/base-app
  ```
- Generate secret key
  ```bash
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- paste in /base-app/webapp/.env
  ```bash
  ENVIRONMENT=DEVELOPMENT
  SECRET_KEY=
  ```
- run the dev server
