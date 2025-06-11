# base app

- ```bash
    django-admin startproject webapp . --template=https://github.com/ycisir/base-app
    ```
-  ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

-  ```bash
  ENVIRONMENT=DEVELOPMENT
  SECRET_KEY=
  ```
