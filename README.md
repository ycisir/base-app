# base app

1. create project folder or create new repository on github
2. create virtual environment and activate it
3. pip install python-decouple django
4. create django project:
   ```bash
   django-admin startproject webapp . --template=https://github.com/ycisir/base-app/archive/refs/heads/main.zip
   ```
5. every time you create a new project, generate a new secret key using the following command:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
6. in the webapp/ directory (where the manage.py file is located), create a .env file. add the following lines to the .env file, replacing your_generated_secret_key with the key generated in the previous step:
   ```bash
   ENVIRONMENT=DEVELOPMENT
   SECRET_KEY=
   ```
7. run the dev server
