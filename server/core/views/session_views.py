from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from core.models import Token
from core.utils.token_utils import TokenUtils

from rest_framework.decorators import api_view
from core.decorators.token_decorators import validate_refresh

User = get_user_model()
token_utils = TokenUtils()

@api_view(['GET'])
@validate_refresh
def sessions(request):
    decoded_refresh = token_utils.decode_refresh_token(request.COOKIES['Refresh'])
    user_id = int(decoded_refresh['user_id'])
    user = User.objects.get(id=user_id)
    token = Token.objects.get_access_token(user)

    if not token:
        token = Token.objects.create_token('access', user)

    response = JsonResponse({'token': token.token}, status=200)

    return response
