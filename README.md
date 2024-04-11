# Django-React Starter App

---

### *Description*

A project that uses Django and React to create a full-stack starter web application.

The backend utilizes Django and Django REST framework to create a RESTful API with user authentication and registration. It uses a simple built-in authentication system using tokens and refresh tokens.

The frontend uses React and React Router to create a single-page application with a simple user interface. A custom api service is used to make requests to the backend.

This is a simple project that is a good launching point for creating a full-stack web application.

### *Contents*

- [Documentation](#documentation)
- [More Docs](#more-docs)
- [Getting Started](#getting-started)
    - [Setting up your .envs](#setting-up-your-envs)
    - [Starting the server](#starting-the-server)
    - [Starting the client](#starting-the-client)
- [Usage](#usage)
    - [Extending the server through the 'core' app](#extending-the-server-through-the-core-app)
    - [Extending the server by a new app](#extending-the-server-by-a-new-app)

### *Documentation*

[Here](/docs/schemas/models.md) is a list of models used in the app.

[Here](/docs/schemas/views.md) is a list of views used in the app.


### *More Docs*

- Getting Started
    - [Client](/docs/getting_started/client.md)
    - [Envs](/docs/getting_started/envs.md)
    - [Server](/docs/getting_started/server.md)
    - [Yarn](/docs/getting_started/yarn.md)
- Schemas
    - [Models](/docs/schemas/models.md)
    - [Session Views](/docs/schemas/session_views.md)
    - [Test Views](/docs/schemas/test_views.md)
    - [User Views](/docs/schemas/user_views.md)
- Usage
    - [Extending the server through the 'core' app](/docs/usage/extend_by_core.md)
    - [Extending the server by a new app](/docs/usage/extend_by_app.md)
- [Demo GIF](/docs/demo.gif)

### *Getting Started*

Anaconda was used to manage the environment for this project. You can install the required packages using the `environment.yml file`. It includes the required packages for the backend and yarn for the frontend.

```bash
conda env create -f environment.yml
```

Activate the environment

```bash
conda activate django-rest
```
#### Setting up your .envs


There are two separate .env files for this project: The client and the server. Example .envs are given in the root directory, but these files should be placed in the client and server directory, respectively, to work. You can copy the .env.example file and rename it to .env in both places. The .env file should not be committed to the repository. It is used to store sensitive information such as API keys and database passwords.

In the server .env file, you will need to set the following variables:
```bash
SUPER_USER
PASSWORD
SERVER_SECRET_KEY
DEBUG

TOKEN_ENCRYPTION_KEY
REFRESH_ENCRYPTION_KEY
ENCODE_ALGORITHM
TOKEN_EXPIRATION_HOURS
REFRESH_EXPIRATION_DAYS
```

The secret key is used in the settings.py file to provide encryption.
The token encryption and the refresh encryption keys are used in the app's token generation. You should use seperate keys for these three variables. You can use [randomkeygen.com](https://randomkeygen.com/) to generate a secret key.

Use integers for the expiration times. The token expiration time is in hours and the refresh expiration time is in days.

The client .env file is used to store the API URL. You will need to set the following variable:

```bash
REACT_APP_API_URL
```

This is the URL that the client will use to make requests to the server. It should be set to the URL of the server. For development, it will be [http://localhost:8000](http://localhost:8000).

#### Starting the server

CD into the root directory and run the following commands to build the database.

```bash
cd django-rest-starter

python manage.py makemigrations
python manage.py migrate
```

You can create a superuser to access the admin panel.

```bash
python manage.py createsuperuser
```

Finally, run the server.

```bash
python manage.py runserver
```

#### Starting the client

yarn package manager is used to manage the client side of the start app. It should have been installed when the environment was created. If not, you can install it using the following command:

```bash
conda install conda-forge::yarn
```

CD into the client directory and run ```yarn``` to install the required packages. Run the following command to start the client:

```bash
yarn start
```

This should start the client on [http://localhost:3000](http://localhost:3000) and open it in your default web browser.

[Here](/docs/getting_started/yarn.md) is the documentation provided by create-react-app that details the other commands that is used throughout development and production.

### *Usage*

#### Extending the server through the 'core' app

The server can be extended by directly adding to the core directory. The core directory has been modularized into separate directories for models, views, and managers. Files can be added into these respective directories. Each directory has an `__init__.py` file that imports the files from that directory. This will need to be modified to include the new files.

If a new model is added, the core directory will look like this:

```bash
core/
    decorators/
    managers/
    migrations/
    models/
        __init__.py
        token_models.py
        user_models.py
        new_models.py   # ***New model file***
    utils/
    views/
```

and the `__init__.py` file in the models directory will look like this:

```python
from .user_models import *
from .token_models import *
from .new_models import *  # ***New model file***

__all__ = [
    'user_models',
    'token_models',
    'new_models'  # ***New model file***
]
```

This way, the new models will be imported if the developer imports by using the following code: `from core.models import *`. The same process can be done for views and managers.

#### Extending the server by a new app

The server can also be extended by creating a new app. This example can be viewed or in full or cloned at the `ca/test-auth` branch in the GitHub repository. The following steps will be a guide to creating a new app called `test_auth` with a new model call `Click`.

<span style="color:red">1.</span> Create a new app using the following command:

```bash
python manage.py startapp test_auth
```

<span style="color:red">2.</span> Add the app to the installed apps in the `server/settings.py` file:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'core',
    'test_auth',    # ***New app***
]
```

<span style="color:red">3.</span> Add a `managers.py` file to the `test_auth` directory. This file will contain the manager for the new model. The `manager.py`, `models.py`, and `views.py` files can also be modularized into separate directories like the `core` app. Here they are all in the same directory for simplicity.

The test_auth directory will look like this:

```bash
test_auth/
    __init__.py
    migrations/
    admin.py
    apps.py
    managers.py  # ***New manager file***
    models.py
    tests.py
    views.py
```

<span style="color:red">4.</span> Add the new model to the `models.py` file:

```python
from django.db import models
from test_auth.managers import ClickManager

class Click(models.Model):

    class Meta:
        db_table = 'test_auth_click'

    id = models.AutoField(primary_key=True)
    clicked_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)

    objects = ClickManager()

    def __str__(self):
        return f'{self.user} clicked at {self.clicked_at}'
```

<span style="color:red">5.</span> Add the new manager to the `managers.py` file:

```python
from django.db import models
from django.utils import timezone


class ClickManager(models.Manager):
    def create_click(self, user):
        new_click = self.create(user=user)
        new_click.save()
        return new_click
    
    def get_click(self, id):
        return self.get(id=id)
    
    def get_clicks_by_user(self, user):
        return self.filter(user=user)
    
    def get_latest_click_by_user(self, user):
        return self.filter(user=user).latest('clicked_at')
```

<span style="color:red">6.</span> Add the new views to the `views.py` file:

```python
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from test_auth.models import Click

from rest_framework.decorators import api_view

from core.decorators.token_decorators import validate_token
from core.decorators.user_decorators import validate_user

User = get_user_model()

@api_view(['POST'])
@validate_token
def click(request):
    user_id = request.data.get('user_id')
    user = User.objects.get(id=user_id)

    click = Click.objects.create_click(user)
    return JsonResponse({'id': click.id, 'clicked_at': click.clicked_at}, status=201)

@api_view(['GET'])
@validate_token
@validate_user
def get_clicks(request, user_id):
    user = User.objects.get(id=user_id)

    clicks = Click.objects.get_clicks_by_user(user)
    return JsonResponse({'clicks': [{'id': click.id, 'clicked_at': click.clicked_at} for click in clicks]}, status=200)
```

<span style="color:red">7.</span> Add the new views to the `server/urls.py` file:

```python
from django.contrib import admin
from django.urls import path
from core.views import (
    register as RegisterView,
    login as LoginView,
    logout as LogoutView,
    me as MeView,
    # test views
    test_token as TestTokenView,
    test_protected as TestProtectedView,
    sessions as SessionsView,
)

from test_auth.views import (   # ***Import new views***
    click as ClickView,
    get_clicks as GetClicksView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('sessions/', SessionsView, name='sessions'),
    path('me/', MeView, name='me'),
    # test views
    path('test-token/', TestTokenView, name='test-token'),
    path('test-protected/', TestProtectedView, name='test-protected'),
    path('click/', ClickView, name='click'),        # ***New url***
    path('get-clicks/<int:user_id>/', GetClicksView, name='get-clicks'),    # ***New url***
]
```

<span style="color:red">8.</span> Run the following commands to create the migrations and migrate the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

<span style="color:red">9.</span> To test the new views, the home page on the client side was modified to include a button that sends a POST request to the new click view. The following code was added to the `client/src/components/home/_home.js` file.

<span style="color:red">10.</span> Run the server and client to test the new views.

![demo gif](/docs/demo.gif)





