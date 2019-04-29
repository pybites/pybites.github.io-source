Title: How to create and serve zip files from Django
Date: 2019-04-27 19:58
Category: Django
Tags: django, zip, snippets, archive
Slug: django-zip
Authors: Bob
Summary: In this article I will show you how to serve zipfiles from Django. We will make a simple app, a download endpoint, add code snippets in the admin back-end, and zip them up in the view. We just used this technique to allow users to export all their committed code on our platform, so I thought it would be useful to share this useful feature!
cover: images/featured/pb-article.png
status: draft

In this article I will show you how to serve zipfiles from Django. We will make a simple app, a download endpoint, add code snippets in the admin back-end, and zip them up in the view. We just used this technique to allow users to export all their committed code on our platform, so I thought it would be useful to share this useful feature!

## Setup

First we make a virtual env, set a secret key in our venv and install Django:

	[bobbelderbos@imac code]$ mkdir django-archive
	[bobbelderbos@imac code]$ cd $_
	[bobbelderbos@imac django-archive]$ alias pvenv
	alias pvenv='/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 -m venv venv && source venv/bin/activate'
	[bobbelderbos@imac django-archive]$ python3.7 -m venv venv
	[bobbelderbos@imac django-archive]$ echo "export SECRET_KEY='abc123.;#'" >> venv/bin/activate
	[bobbelderbos@imac django-archive]$ source venv/bin/activate
	(venv) [bobbelderbos@imac django-archive]$ pip install django
	Collecting django
	...
	Successfully installed django-2.2 pytz-2019.1 sqlparse-0.3.0

Now let's create a project and app in Django:

	(venv) [bobbelderbos@imac django-archive]$ django-admin startproject snippets .
	(venv) [bobbelderbos@imac django-archive]$ django-admin startapp archive

The dot is to prevent Django from making an extra folder. I end up with the following files:

	(venv) [bobbelderbos@imac django-archive]$ tree -L 2
	.
	├── archive
	│   ├── __init__.py
	│   ├── admin.py
	│   ├── apps.py
	│   ├── migrations
	│   ├── models.py
	│   ├── tests.py
	│   └── views.py
	├── manage.py
	├── snippets
	│   ├── __init__.py
	│   ├── settings.py
	│   ├── urls.py
	│   └── wsgi.py
	└── venv
		├── bin
		├── include
		├── lib
		├── pip-selfcheck.json
		└── pyvenv.cfg

	7 directories, 13 files

Make sure we add the new app to Django's config:

snippets/settings.py

	INSTALLED_APPS = [
		...
		# own apps
		'archive',
	]

Lastly let's sync the DB and create a superuser to login to Django's admin back-end:

	(venv) [bobbelderbos@imac django-archive]$ python manage.py migrate
	Operations to perform:
	Apply all migrations: admin, auth, contenttypes, sessions
	Running migrations:
	Applying contenttypes.0001_initial... OK
	Applying auth.0001_initial... OK
	Applying admin.0001_initial... OK
	Applying admin.0002_logentry_remove_auto_add... OK
	Applying admin.0003_logentry_add_action_flag_choices... OK
	Applying contenttypes.0002_remove_content_type_name... OK
	Applying auth.0002_alter_permission_name_max_length... OK
	Applying auth.0003_alter_user_email_max_length... OK
	Applying auth.0004_alter_user_username_opts... OK
	Applying auth.0005_alter_user_last_login_null... OK
	Applying auth.0006_require_contenttypes_0002... OK
	Applying auth.0007_alter_validators_add_error_messages... OK
	Applying auth.0008_alter_user_username_max_length... OK
	Applying auth.0009_alter_user_last_name_max_length... OK
	Applying auth.0010_alter_group_name_max_length... OK
	Applying auth.0011_update_proxy_permissions... OK
	Applying sessions.0001_initial... OK

	(venv) [bobbelderbos@imac django-archive]$ python manage.py createsuperuser
	Username (leave blank to use 'bobbelderbos'): bob
	Email address:
	Password:
	Password (again):
	This password is too short. It must contain at least 8 characters.
	Bypass password validation and create user anyway? [y/N]: y
	Superuser created successfully.

## Create routes

In the main app that was created with the `startproject` command we add the following routes:

snippets/urls.py

	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('', include('archive.urls', namespace='archive')),
	]

I use the admin app that Django comes equipped with and make a new link to the `urls.py` file of the `archive` app we created. Let's create that one next:

archive/urls.py

	from django.urls import path

	from . import views

	app_name = 'bites'
	urlpatterns = [
		path('download/', views.download, name='download')
	]

This will be the download endpoint we will write later in `views.py`. Let's first define a model to hold the code snippets.

## Create a Script model

In our `archive` app we make a simple model which we will sync to a real DB table and it will hold code snippets:

archive/models.py

	from django.db import models


	class Script(models.Model):
		name = models.CharField(max_length=100)
		code = models.TextField()
		added = models.DateTimeField(auto_now_add=True)

		def __str__(self):
			return self.name

		class Meta:
			ordering = ['-added']

We inherit all goodness from Django's `Model` class, define `__str__` as best practice when debugging objects, and add `ordering` so last added snippets will show up first.

Now we have to commit this model to the DB so we use the `manage.py` interface again

First we need to stub out the `downloads` function otherwise we get: `AttributeError: module 'archive.views' has no attribute 'download'`, so add this to archive/views.py:

	def download(request):
		pass

Then run:

	(venv) [bobbelderbos@imac django-archive]$ python manage.py makemigrations
	Migrations for 'archive':
	archive/migrations/0001_initial.py
		- Create model Script
	(venv) [bobbelderbos@imac django-archive]$ python manage.py migrate
	Operations to perform:
	Apply all migrations: admin, archive, auth, contenttypes, sessions
	Running migrations:
	Applying archive.0001_initial... OK

I am just using the default `sqlite` DB, we can use schema to see what `migrate` created:

	(venv) [bobbelderbos@imac django-archive]$ sqlite3 db.sqlite3
	SQLite version 3.24.0 2018-06-04 19:24:41
	Enter ".help" for usage hints.
	sqlite> .table
	... other tables ...
	archive_script              <== our new table
	sqlite> .schema  archive_script
	CREATE TABLE IF NOT EXISTS "archive_script" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "code" text NOT NULL, "added" datetime NOT NULL);

## Add some code snippets via Django's admin interface

To be able to work with the new model from the admin interface we need to register it:

archive/admin.py

	from django.contrib import admin

	from .models import Script


	class ScriptAdmin(admin.ModelAdmin):
		pass
	admin.site.register(Script, ScriptAdmin)

Now let's serve up the app:

$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
April 27, 2019 - 16:30:55
Django version 2.2, using settings 'snippets.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Going to `http://localhost:8000/admin` and login with the superuser I created, I can add code snippets to our new Script model / table:


Let's add some snippets from some Bites I coded lately ;)



## Serve up a zipfile with all code snippets in the view




---

That's it, a small admin tailored app to serve code files in zipfile via a Django endpoint. 

One enhancement would be to lock this down to users not logged in. Django makes this easy, just add this snippet at the top of `download` returning a 401 (not authorized):

	if not request.user.is_authenticated:
		return HttpResponse(status=401)

(`request` already gets passed into the view by default)

And this is how the feature looks on the platform with real code snippets:


Keep Calm and Code in Python!

-- Bob
