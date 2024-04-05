# Django-React Starter App

---

### *Description*

A project that uses Django and React to create a full-stack starter web application.

The backend utilizes Django and Django REST framework to create a RESTful API with user authentication and registration. It uses djangorestframework_simplejwt and a little extra logic to provide a token-based authentication system.

The frontend uses React and React Router to create a single-page application with a simple user interface. It uses Axios to make requests to the backend API.

This is a simple project that is a good launching point for creating a full-stack web application.

### *Documentation*

[Here](/docs/schemas/models.md) is a list of models used in the app.

[Here](/docs/schemas/views.md) is a list of views used in the app.

### *Getting Started*

Anaconda was used to manage the environment for this project. You can install the required packages using the environment.yaml file. It includes the required packages for the backend and yarn for the frontend.

```bash
conda env create -f environment.yml
```

Activate the environment

```bash
conda activate django-rest
```
![setting up the .envs](/docs/getting_started/envs.md)

![starting the server](/docs/getting_started/server.md)

![starting the client](/docs/getting_started/client.md)
