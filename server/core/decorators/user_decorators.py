from core.managers.token_managers import TokenManager

from django.http import JsonResponse

def validate_user(func):
    def wrapper(request, user_id, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'error': 'Token is required'}, status=401)
        
        decoded_token = TokenManager().decode_token(token)
        if not decoded_token:
            return JsonResponse({'error': 'Invalid token'}, status=401)
        
        if decoded_token['user_id'] != user_id:
            return JsonResponse({'error': 'Invalid user'}, status=401)
        
        return func(request, user_id, *args, **kwargs)
    
    return wrapper
