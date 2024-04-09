from django.db import models
from test_auth.managers import ClickManager

class Click(models.Model):

    class Meta:
        db_table = 'test_auth_click'

    id = models.AutoField(primary_key=True)
    clicked_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)

    objects = ClickManager()

    def __str__(self):
        return f'{self.user} clicked at {self.clicked_at}'