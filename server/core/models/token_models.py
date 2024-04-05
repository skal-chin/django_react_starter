from django.db import models

from core.managers import TokenManager

class Token(models.Model):

    class Meta:
        db_table = 'core_token'

    TOKEN_TYPE = (
        ('access', 'Access'),
        ('refresh', 'Refresh'),
    )
    
    id = models.AutoField(primary_key=True)
    token_type = models.CharField(max_length=10, choices=TOKEN_TYPE)
    token = models.CharField(max_length=255)
    expires = models.DateTimeField()
    issued_at = models.DateTimeField()
    is_valid = models.BooleanField(default=True)
    user = models.ForeignKey('core.CustomUser', on_delete=models.CASCADE)

    objects = TokenManager()

    def __str__(self):
        return f'{self.token_type} token for {self.user}'
