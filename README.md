# baseball-players
In the Django project folder `myproject` is a basic site `myproject` with an app called `players`, the focus of this project. There is also a Django project called `djangotutorial`, where some of the tutorial on the Django website was done. Notes taken from doing that tutorial are below.

To set up the main project:
- install `python` (`python3` is used for the command here), `django`, and `python3-django` if needed:
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install pip
$ pip install django
$ sudo apt install python3-django
```
- navigate to `baseball-players/myproject` in a terminal
- confirm there is a file `players.json`
- run `python3 manage.py migrate`
- import the players by running `python3 manage.py shell < importPlayers.py`
- run `python3 manage.py runserver` to start the app
- create a super user with `python3 manage.py createsuperuser`
- the imported data should be available to manage in the Django-project-generated admin site at http://127.0.0.1:8000/admin
- navigate to http://127.0.0.1:8000/players/ to view the app on the homepage

# Project Timeline
- time estimates in parentheses
- setup, looking at data, models (1 hr 30 min)
- importing data (1 hr 30 min)
    - use importPlayers.py
        - `python3 manage.py shell < importPlayers.py `
- basic views and apis (2 hrs)
    - tried to nest views but did not have time to figure out a good way to do that
- views and styling (2 hrs 15 min)
- async calls (45 min)
    - unsuccessful
    - tried to make async views
    - tried to make async model methods

# Tutorial Notes (for myself)
https://docs.djangoproject.com/en/5.1/intro/tutorial01/
## Basic Setup (35 min)
```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install pip
$ pip install django
$ sudo apt install python3-django
$ django-admin startproject myproject
$ cd myproject
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
    student/student
$ python3 manage.py runserver
```
- view at http://127.0.0.1:8000
- admin interface at http://127.0.0.1:8000/admin
    - login student/student
- create new apps with
    ```
    $ python3 manage.py startapp appname
    ```
- manage static files by adding them to
    `STATICFILES_DIRS` in `settings.py`
- store html templates in directory named templates and configure `TEMPLATES` setting in `settings.py`
## Part 1 (20 min)
```
$ mkdir djangotutorial
$ django-admin startproject mysite djangotutorial
$ cd djangotutorial
$ python3 manage.py runserver
$ python3 manage.py startapp polls
```
## Part 2 (1 hr)
```
$ cd djangotutorial
$ python3 manage.py migrate
```
- add classes to `polls/models.py`
add `"polls.apps.PollsConfig"` to `INSTALLED_APPS` in `mysite/settings.py`
```
$ python3 manage.py makemigrations polls
$ python3 manage.py sqlmigrate polls 0001
    to see sql that migration would run
$ python3 manage.py check
    to check for problems in project without making migrations or touching db
$ python3 manage.py migrate
    to actually run that sql
```
making model changes:
- change models in models.py
- run python3 manage.py makemigrations to create migrations for those changes
- python3 manage.py migrate to apply those changes to db

### Playing with the API
```
$ python3 manage.py shell
```
https://docs.djangoproject.com/en/5.1/topics/db/queries/

### Introducing the Django Admin
```
$ python3 manage.py createsuperuser
    admin/admin admin@example.com
$ python3 manage.py runserver
```
view admin site at http://127.0.0.1:8000/admin/

## Part 3 (45 min)
- add views to `polls/views.py`
- add url patterns to `polls/urls.py`
- create dir `polls/templates`
- create dir `polls/templates/polls`
- create file `polls/templates/polls/index.html`
    - can refer to this template in Django as polls/index.html
- more about templates
    - https://docs.djangoproject.com/en/5.1/topics/templates/

## Part 4 (30 min)
- update `polls/views.py`
- create `polls/templates/polls/results.html`

### Use Generic Views
- update `polls/urls.py`
- update `polls/views.py`

## Asynchronous calls (1 hr)
- async views
- async model methods
- async model @class methods
