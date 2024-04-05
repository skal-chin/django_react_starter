from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if not email:
            raise ValueError('email field is required')
        
        email = self.normalize_email(email)
        username = username if username else email.split('@')[0]
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, username=None):
        user = self.create_user(email, password, username)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
    def unique_email(self, email):
        if self.filter(email=email).exists():
            return False
        return True
    
    def unique_username(self, username):
        if self.filter(username=username).exists():
            return False
        return True
    
    def get_user(self, id):
        return self.get(id=id)
    
    def deactivate_user(self, user):
        user.is_active = False
        user.save()
        return
    
    def get_user_by_email(self, email):
        return self.get(email=email)
    
    def get_user_by_username(self, username):
        return self.get(username=username)
    
    def user_exists(self, email):
        return self.filter(email=email).exists()

