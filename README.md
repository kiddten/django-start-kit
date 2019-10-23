#### Create virtual env
```shell script
python -m venv venv
```

#### Activate venv
```shell script
source venv/bin/activate
```

#### Install django
```shell script
pip install Django
```

#### Bootstrap project with django
```shell script
django-admin startproject myapp
```

#### Test run
```shell script
python manage.py runserver
```

#### Run default migrations
```shell script
python manage.py migrate
```

#### Create new sup application
```shell script
python manage.py startapp subapp
```

#### Move subapp to myapp/apps/ and add to settings.py
```python
import os
import sys
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
```

#### Create migrations according to models
```shell script
python manage.py makemigrations
```
Don't forget to add your app to `INSTALLED_APPS`

Add `'subapp.apps.SubappConfig',` (subapp.apps) to `INSTALLED_APPS`

#### Prints the SQL statements for the named migration
```shell script
python manage.py sqlmigrate subapp 0001
```

#### There are will be internal table with info about current state of migrations
`django migrations` in your db

#### Run custom django shell
```shell script
python manage.py shell
```

### Basic orm examples
```python
from subapp.models import *

# create new entity
Article(field_name1='', field_name2='')

Article.objects.all()

obj.save() # save object state to db

# get by id
Article.objects.get(id=1)

Article.objects.filter(article_title__startswith='ti')

a.comment_set.all() # get related records by foreign key

a.comment_set.create(author_name='a1', comment_text='comment') # create related record

a.comment_set.count()

latest_article_list = Article.objects.order_by('-pub_date')[:10]
```

#### Create superuser for admin
```shell script
python manage.py createsuperuser
```

#### settings.py change lang
```python
LANGUAGE_CODE = 'en-us'
```

#### Register models in admin 
In subapp admin.py add
```python
from django.contrib import admin
admin.site.register(Article)
```

#### Add to model to translate or add verbose name for models in admin
```python
class Meta:
    verbose_name = 'Article'
    verbose_name_plural = 'Articles'
```

Same for `AppConfig` with verbose_name fot i18n

#### Install style for admin
https://django-grappelli.readthedocs.io/en/latest/quickstart.html#installation

#### Collect static files in a single location
```shell script
python manage.py collectstatic
```

#### Don't forget to configure STATIC_ROOT constant
```python
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
```

#### Don't forget to enable django template syntax in pycharm setting
> python template languages

#### CSRF in templates
```python
{% csrf_token %}
```