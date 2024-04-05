from core.models.token_models import Token

from django.http import JsonResponse

def validate_token(func):
    def wrapper(request, *args, **kwargs):
        token_header = request.headers.get('Authorization')
        token = token_header.split(' ')[1] if token_header else None

        if not token:
            return JsonResponse({'error': 'Token is required'}, status=401)
        
        try:
            t = Token.objects.get(token=token)
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Invalid token'}, status=401)
                    
        if not Token.objects.is_valid_token(token):
            return JsonResponse({'error': 'Invalid token'}, status=401)
        
        return func(request, *args, **kwargs)
    return wrapper

def validate_refresh(func):
    def wrapper(request, *args, **kwargs):
        refresh_cookie = request.COOKIES.get('Refresh')
        if not refresh_cookie or refresh_cookie == 'null':
            return JsonResponse({'error': 'Refresh token is required'}, status=401)
        
        try:
            t = Token.objects.get(token=refresh_cookie)
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Invalid refresh token'}, status=401)

        if not Token.objects.is_valid_token(refresh_cookie):
            return JsonResponse({'error': 'Invalid refresh token'}, status=401)
        
        return func(request, *args, **kwargs)
    return wrapper