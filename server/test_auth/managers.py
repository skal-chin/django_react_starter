from django.db import models
from django.utils import timezone


class ClickManager(models.Manager):
    def create_click(self, user):
        new_click = self.create(user=user)
        new_click.save()
        return new_click
    
    def get_click(self, id):
        return self.get(id=id)
    
    def get_clicks_by_user(self, user):
        return self.filter(user=user)
    
    def get_latest_click_by_user(self, user):
        return self.filter(user=user).latest('clicked_at')