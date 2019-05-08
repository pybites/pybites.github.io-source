Title: How to Create and Serve Zipfiles from Django
Date: 2019-05-08 08:00
Category: Django
Tags: Django, zipfile, snippets, archive, response, request, admin, DB, sqlite3, migrations, virtualenv
Slug: django-zipfiles
Authors: Bob
Summary: We added support [to our platfom](https://codechalleng.es) for bulk downloading of all your code submissions. This feature required creating and serving up zipfiles through Django. In this article I show you how to do it creating a simple Django app collecting code snippets through the admin interface, and serving them up in a zipfile via a download endpoint. Let's dive straight in ...

We added support [to our platfom](https://codechalleng.es) for bulk downloading of all your code submissions. This feature required creating and serving up zipfiles through Django. In this article I show you how to do it creating a simple Django app collecting code snippets through the admin interface, and serving them up in a zipfile via a download endpoint. Let's dive straight in ...

## Setup

First we make a virtual env, set a secret key in our venv and install Django:

	[bobbelderbos@imac code]$ mkdir django-archive
	[bobbelderbos@imac code]$ cd $_
	[bobbelderbos@imac django-archive]$ python3.7 -m venv venv
	[bobbelderbos@imac django-archive]$ echo "export SECRET_KEY='abc123.;#'" >> venv/bin/activate
	[bobbelderbos@imac django-archive]$ source venv/bin/activate
	(venv) [bobbelderbos@imac django-archive]$ pip install django
	Collecting django
	...
	Successfully installed django-2.2 pytz-2019.1 sqlparse-0.3.0

Now let's create a project and app in Django. Don't forget the extra dot in the `startproject` command to not create an extra subdirectory.

	(venv) [bobbelderbos@imac django-archive]$ django-admin startproject snippets .
	(venv) [bobbelderbos@imac django-archive]$ django-admin startapp archive
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
		...

Make sure we add the new app to Django's config:

snippets/settings.py

	INSTALLED_APPS = [
		...
		# own apps
		'archive',
	]

While here, let's also load the secret key from our venv (`venv/bin/activate`) as defined earlier:

	SECRET_KEY = os.environ['SECRET_KEY']

Lastly let's sync the pending migrations to our default sqlite DB and create a superuser to access Django's admin back-end:

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

In the main app `snippets`, that was created with the `startproject` command, we add the following routes:

snippets/urls.py

	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
		path('admin/', admin.site.urls),
		path('', include('archive.urls', namespace='archive')),
	]

Apart from the default admin routes (`admin.site.urls`), we namespace the `archive` app's routes, defining them in the app:

archive/urls.py

	from django.urls import path

	from . import views

	app_name = 'archive'
	urlpatterns = [
		path('download/', views.download, name='download')
	]

This will be the download endpoint that will serve the zipfile, we will write that code in a bit. First let's define the model (DB table) that will hold our code snippets.

## Create a Script model

In our `archive` app we make this simple model and sync it to the DB:

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

We inherit all goodness from Django's `Model` class. The `added` datetime gets automatically populated upon insert. Defining a `__str__` on the class makes it easier to inspect the objects when debugging (or in Django's interactive shell). And we can use the inner `Meta` class to set further behaviors, in this case let's show most recently added snippets first. 

Now we have to commit ("migrate") this model to the DB which is easy using Django's `manage.py`. However first we need to stub out the `download` function we defined in `archive/urls.py`, otherwise we get: `AttributeError: module 'archive.views' has no attribute 'download'` upon migration. Add this code to `archive/views.py`:

archive/views.py

	def download(request):
		pass

Now it should work:

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

## Django's admin interface

To be able to work with the new model from the admin interface we need to register it. Add this code to the `archive/admin.py` module:

archive/admin.py

	from django.contrib import admin

	from .models import Script


	class ScriptAdmin(admin.ModelAdmin):
		pass
	admin.site.register(Script, ScriptAdmin)

Now let's spin up the dev server. As I leave it running in the foreground I use a second terminal:

	$ cd /Users/bbelderbos/code/django-archive
	$ source venv/bin/activate
	(venv) [bbelderbos@imac django-archive]$ python manage.py runserver
	Watching for file changes with StatReloader
	Performing system checks...

	System check identified no issues (0 silenced).
	May 08, 2019 - 02:17:32
	Django version 2.2, using settings 'snippets.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CONTROL-C.

Now I can access `http://localhost:8000/admin` and login with the superuser I created earlier. At this point we should see the new model:

![new model in admin]({filename}/images/django-zip/admin.png)

Let's add some small code snippets from [our tips page](https://codechalleng.es/tips):

![3 snippets added]({filename}/images/django-zip/3-snippets.png)

![adding snippet 1]({filename}/images/django-zip/snippet1.png)

![adding snippet 2]({filename}/images/django-zip/snippet2.png)

![adding snippet 3]({filename}/images/django-zip/snippet3.png)

## Serving up a zipfile

Now let's create a zipfile with all the code snippets stored in the DB. We do this in the `download` view we stubbed out earlier:

archive/views.py

	import zipfile

	from django.http import HttpResponse

	from .models import Script

	README_NAME = 'README.md'
	README_CONTENT = """
	## PyBites Code Snippet Archive

	Here is a zipfile with some useful code snippets.

	Produced for blog post https://pybit.es/django-zipfiles.html

	Keep calm and code in Python!
	"""
	ZIPFILE_NAME = 'pybites_codesnippets.zip'


	def download(request):
		"""Download archive zip file of code snippets"""
		response = HttpResponse(content_type='application/zip')
		zf = zipfile.ZipFile(response, 'w')

		# create the zipfile in memory using writestr
		# add a readme
		zf.writestr(README_NAME, README_CONTENT)

		# retrieve snippets from ORM and them to zipfile
		scripts = Script.objects.all()
		for snippet in scripts:
			zf.writestr(snippet.name, snippet.code)

		# return as zipfile
		response['Content-Disposition'] = f'attachment; filename={ZIPFILE_NAME}'
		return response

We use Django's `HttpResponse` object which we have to give a `Content-Disposition` attribute. To directly serve up the resulting zipfile, not writing it to disk, I use `zipfile`'s `writestr`. Getting the snippets from Django's ORM is as easy as: `Script.objects.all()`. I also added a _README_ file.

Now visit the download endpoint: http://localhost:8000/download -> A zipfile should automatically download to your desktop:

![download the zipfile]({filename}/images/django-zip/download-endpoint.png)

Let's see if it worked by unzipping the obtained zipfile into a tmp directory:

	[bbelderbos@imac Downloads]$ mkdir tmp
	[bbelderbos@imac Downloads]$ mv pybites_codesnippets.zip tmp
	[bbelderbos@imac Downloads]$ cd tmp
	[bbelderbos@imac tmp]$ unzip pybites_codesnippets.zip
	Archive:  pybites_codesnippets.zip
	extracting: README.md
	extracting: flatten.py
	extracting: zipping.py
	extracting: enumerate.py

	[bbelderbos@imac tmp]$ cat README.md

	## PyBites Code Snippet Archive

	Here is a zipfile with some useful code snippets.

	Produced for blog post https://pybit.es/django-zipfile

	Keep calm and code in Python!

	[bbelderbos@imac tmp]$ for i in *py; do echo "== $i =="; cat $i; echo ; done
	== enumerate.py ==
	names = 'bob julian tim sara'.split()
	for i, name in enumerate(names, 1):
		print(i, name)
	== flatten.py ==
	list_of_lists = [[1, 2], [3], [4, 5], [6, 7, 8]]
	flattened = sum(list_of_lists, [])
	print(flattened)
	== zipping.py ==
	names = 'bob julian tim sara'.split()
	ages = '11 22 33 44'.split()
	print(dict(zip(names, ages)))

---

Cool! So there you have it: a small Django app with a single model and view to serve zipfiles :)

One enhancement would be to lock this down for users that are not logged in. Django makes this easy, just add this the following code at the top of the `download` function, returning a 401 (and _toast_ message) if the user is not authenticated:

	from django.contrib import messages
	...
	def download(request):
		"""Download archive zip file of code snippets"""

    	if not request.user.is_authenticated:
        	messages.error(request, 'Need to be logged in to access this endpoint')
        	return HttpResponse(status=401)

		... 

The full code for this blog post is [here](http://github.com/pybites/blog_code/django-archive).

---

If you saved some code for Bite exercises [on our platform](http://codechalleng.es) you can check out this feature scrolling to the bottom of [the settings page](http://codechalleng.es/settings) ...

I hope this was useful and let us know if there are other Django related topics you'd like to see covered here ...

Keep Calm and Code in Python!

-- Bob
