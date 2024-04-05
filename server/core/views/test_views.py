import jwt
from server.settings import ENV

from django.utils import timezone
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from core.decorators.token_decorators import validate_token

@api_view(['GET'])
@permission_classes([AllowAny])
def test_token(request):
    user = {
        'id': 1,
        'email': 'fake',
        'username': 'fake',
    }
    token = jwt.encode({
        'user': user['id'],
        'exp': timezone.now() + timezone.timedelta(hours=int(ENV('TOKEN_EXPIRATION_HOURS'))),
        'iat': timezone.now(),
    }, ENV('TOKEN_ENCRYPTION_KEY'), algorithm='HS256')

    print(token)
    print('Decoded token:', jwt.decode(token, ENV('TOKEN_ENCRYPTION_KEY'), algorithms=['HS256']))
    return JsonResponse({'message': 'token is valid'}, status=200)

@api_view(['GET'])
@validate_token
def test_protected(request):
    return JsonResponse({'message': 'protected endpoint'}, status=200)