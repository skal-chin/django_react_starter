# Django-React Starter App

---

### *Description*

A project that uses Django and React to create a full-stack starter web application.

The backend utilizes Django and Django REST framework to create a RESTful API with user authentication and registration. It uses a simple built-in authentication system using tokens and refresh tokens.

The frontend uses React and React Router to create a single-page application with a simple user interface. A custom api service is used to make requests to the backend.

This is a simple project that is a good launching point for creating a full-stack web application.

### *Documentation*

[Here](/docs/schemas/models.md) is a list of models used in the app.

[Here](/docs/schemas/views.md) is a list of views used in the app.

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
