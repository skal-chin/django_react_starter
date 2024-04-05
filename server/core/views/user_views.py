from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from core.models import Token
from core.utils.token_utils import TokenUtils
from core.utils.validate_email import validate_email
from core.utils.validate_password import validate_password

from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from core.decorators.token_decorators import validate_token
from core.decorators.user_decorators import validate_user

User = get_user_model()
token_utils = TokenUtils()

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = request.data.get('username')

    if not email or not password:
        return JsonResponse({'error': 'email and password are required'}, status=400)
    if not User.objects.unique_email(email):
        return JsonResponse({'error': 'email already in use'}, status=400)
    if username and not User.objects.unique_username(username):
        return JsonResponse({'error': 'username already in use'}, status=400)
    
    if not validate_email(email):
        return JsonResponse({'error': 'invalid email'}, status=400)
    if not validate_password(password):
        return JsonResponse({'error': 'invalid password'}, status=400)

    user = User.objects.create_user(email, password, username)
    
    token = Token.objects.create_token('access', user)
    refresh = Token.objects.create_token('refresh', user)

    response = JsonResponse({'id': user.id, 'username': user.usernamen, 'token': token.token}, status=201)
    response.set_cookie('Refresh', refresh.token, httponly=True)
    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return JsonResponse({'error': 'email and password are required'}, status=400)
    
    if not User.objects.user_exists(email):
        return JsonResponse({'error': 'invalid email or password'}, status=400)
    
    user = User.objects.get_user_by_email(email)
    
    if not user.check_password(password):
        return JsonResponse({'error': 'invalid email or password'}, status=400)
    
    
    token = Token.objects.create_token('access', user)
    refresh = Token.objects.create_token('refresh', user)

    response = JsonResponse({'id': user.id, 'username': user.username, 'token' : token.token}, status=200)
    response.set_cookie('Refresh', refresh.token, httponly=True)
    return response

@api_view(['GET'])
@validate_token
def logout(request):
    decoded_token = token_utils.decode_refresh_token(request.COOKIES['Refresh'])
    user_id = int(decoded_token['user_id'])
    user = User.objects.get(id=user_id)
    Token.objects.delete_tokens_by_user(user)
    response = JsonResponse({'message': 'logged out'}, status=200)
    response.delete_cookie('Refresh')
    return response

@api_view(['GET'])
@validate_token
def me(request):
    token = request.headers.get('Authorization')
    decoded_token = token_utils.decode_token(token)
    user_id = int(decoded_token['user_id'])
    user = User.objects.get(id=user_id)
    return JsonResponse({'id': user.id, 'username': user.username}, status=200)

