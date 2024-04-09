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
    return JsonResponse({'user_id': user_id, 'click_id': click.id}, status=201)

@api_view(['GET'])
@validate_token
@validate_user
def get_clicks(request, user_id):
    user = User.objects.get(id=user_id)

    clicks = Click.objects.get_clicks_by_user(user)
    return JsonResponse({'clicks': [{'id': click.id, 'clicked_at': click.clicked_at} for click in clicks]}, status=200)

