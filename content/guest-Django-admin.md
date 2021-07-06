# Working with the admin interface in Django 

Django’s admin site is one of the most fascinating parts of Django. Anyone coming from a different framework to Django or someone just starting to learn about the web with Django. It’s amazing to see such a sophisticated admin site you get out of the box. 

Admin site was initially used as an internal CMS at [Lawrence Journal-World](https://www2.ljworld.com/) and in 2005 was released as part of Django. Now, admin’s interface is mainly used by site administrators and occasionally assists Django developers. 

Getting started with Django Admin

Now that we know what a django admin is, let’s put on our developer hat and see the admin interface in action. 

Let’s create a Django project called PyBites and add a blog app in it. 

```
django-admin startproject PyBites 
django-admin startapp blog 
```

Seeing project structure we can see that there already exists an `admin.py` file. 

```
.
├── PyBites
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── manage.py

```

Let us register the `blog` app in `settings.py` so that django knows we have created the app and later we would be using it to access the admin interface.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```
Once you add the app in the `INSTALLED_APPS` let's do our first migration. In the base directory of the project, run the following command:

```
python manage.py migrate  
```

A successful migration will result something like this:

```
> python manage.py migrate            
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
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

Throught out the blog post we would be invloved primarly with the `blog/admin.py` file. Currently that file contains the following code snippet:

```
from django.contrib import admin

# Register your models here.
```

Let's how does an admin interface look for a fresh project. To do that, we would need to create a super user first to access the admin interface in blog app. 

```
python manage.py createsuperuser
```

Once your done with creating the super user, let's run dev server and see how a fresh admin interface looks like. Just run the dev server with the following command:

```
python manage.py runserver 
```

If everything goes well, you would see something like this in the terminal.

```
> python manage.py runserver      
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 17, 2021 - 15:54:58
Django version 3.1.5, using settings 'PyBites.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

To access the admin interface just login into the following URL `http://127.0.0.1:8000/admin` and login with your credentials that you used to create superuser.

<!-- Insert admin panel screenshot here -->

You would see we have almost no infor here besied the inbuilt `Authentication and Authorization` which has `Groups` and `Users` 

* Groups are 

* Users are 

For now the admin looks a bit stale and does not help us in any way. That's because we have no added any models in it yet. Since it's a blog app we are dealing with let's start by creating a model for our app.

A basic model for `Post` that would have some basic fields for a blog post like title, author, body etc.  

```
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

```

Now let's add a migration for `blog` app.

```
python manage.py makemigrations blog
python manage.py migrate blog
```

A successful migration will look something like this:

```
> python manage.py makemigrations blog
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```

```
> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK
```

Finally register this model in `blog/admin.py` so that we can check the model out in the admin interface. 

```
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Once the model is registered, restart the dev server and login to the admin interface.

<!-- Insert picture with Post model in the admin interface -->

Notice the Post model under the app name in the admin interface. 

Most of the developers who migrate to Django are blown away by the simplicity of the admin interface of it. With just some basic configuration, we were able to make a fully functional admin interface. 

Let's see the admin in action by creating a blog post entry to our database, this can be done by clicking add button next to `Post` model. 

A post model UI would open up with the fields that we mentioned in our `Post` model.

<!-- Insert picture with Post model UI with empty model fields -->

Publish field has a interactive Date and Time field, Status field has a dropdown and Author field be default has your username with an option to add another user. How cool it that! 

Though on adding a post admin shows the post in a weird manner, something like `Post object (1)`

<!-- Insert picture with Post object (1) entry -->

Would be nice if we could see the blog heading atleast right ? Let's fix that.

Let's add the `__str__` in the our models that should fix that. 

```
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(
        User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
```
<!-- 

Things to add in the blog

* List View

* Filters

* Search 

* Django models available for is_staff=True

* Securing Django admin by moving the admin URL

* Django admin honeypot

-->
