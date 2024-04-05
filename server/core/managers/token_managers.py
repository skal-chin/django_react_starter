from django.db import models
from django.utils import timezone
from core.utils.token_utils import TokenUtils

class TokenManager(models.Manager):
    def create_token(self, token_type, user):

        token, expires, issued_at = TokenUtils().create_token(token_type, user, return_info=True)

        new_token = self.create(
            token_type=token_type,
            token=token,
            expires=expires,
            issued_at=issued_at,
            is_valid=True,
            user=user,
        )

        new_token.save()
        return new_token
    
    def get_token(self, id):
        return self.get(id=id)
    
    def get_token_by_user(self, user):
        return self.filter(user=user).latest('issued_at')
    
    def get_user_tokens(self, user):
        return self.filter(user=user)
    
    def is_valid_token(self, token):
        if self.filter(token=token, is_valid=True).exists():
            return True
        return False
    
    def invalidate_token(self, token):
        token.is_valid = False
        token.save()

    def purge(self):
        self.filter(expires__lt=timezone.now()).delete()

    def get_all_tokens(self):
        return self.all()
    
    def get_valid_tokens(self):
        return self.filter(expires__gt=timezone.now(), is_valid=True)
    
    def delete(self, token):
        token.delete()
        return token
    
    def delete_tokens_by_user(self, user, token_type=None):
        if token_type:
            self.filter(user=user, token_type=token_type).delete()
        else:
            self.filter(user=user).delete()
        return True
        
    def get_refresh_token(self, user):
        return self.filter(user=user, token_type='refresh', is_valid=True).latest('issued_at')
    
    def get_access_token(self, user):
        return self.filter(user=user, token_type='access', is_valid=True).latest('issued_at')