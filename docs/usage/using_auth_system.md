#### Using the authentication system

The authentication system is built into the server with the following views ready to use:

- `/register/` - POST request to register a new user. Requires a username, email, and password.
- `/login/` - POST request to login a user. Requires a username and password.
- `/logout/` - GET request to logout a user. Requires a token.
- `/me/` - GET request to get the user's information. Requires a token.
- `/sessions/` - GET request to retrieve a token based on the Refresh cookie. Requires a refresh cookie.

The system uses access and refresh tokens to authenticate users. The access token is used to access protected views and the refresh token is used to stayed logged in and request a new access token when the old one expires. These tokens are encrypted and stored in the database so they can be checked against a user's request credentials. The tokens are generated using the `core.utils.token_utils` module.

The views are protected by decorators that check the user's token. The `core.decorators.token_decorators` module contains the decorators that are used to protect the views. The `validate_token` decorator is used to check the user's access token and the `validate_refresh` decorator is used to check the user's refresh token. To protect a view, the decorator is added above the view function like so:

```python
from django.http import JsonResponse
...
# import the decorator
from core.decorators.token_decorators import validate_token

@api_view(['GET'])
@validate_token     # add the decorator
def protected_view(request):
    return JsonResponse({'message': 'This is a protected view'}, status=200)

@api_view(['GET']) # this view is not protected
def unprotected_view(request): #
    return JsonResponse({'message': 'This is an unprotected view'}, status=200)
```

Use the `validate_token` decorator for any views that require a token and is request private information. The `validate_refresh` decorator only needs to be used for the `/sessions/` view or anything that only requires a refresh token.

The `validate_user` decorator is used to check if the user requesting the data is the same as the user in the token. This decorator requires a `user_id` parameter in the URL. It is used like so:

```python
from django.http import JsonResponse
...
# import the decorator
from core.decorators.user_decorators import validate_user

@api_view(['GET'])
@validate_token
@validate_user
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    return JsonResponse({'user': {'id': user.id, 'username': user.username, 'email': user.email}}, status=200)
```

The URL for this view would look like this: `/get-user/<int:user_id>/`. The `user_id` parameter is required in the URL.