import jwt
from server.settings import ENV
from django.utils import timezone

class TokenUtils():
    def __init__(self):
        self.TOKEN_ENCRYPTION_KEY = ENV('TOKEN_ENCRYPTION_KEY')
        self.REFRESH_ENCRYPTION_KEY = ENV('REFRESH_ENCRYPTION_KEY')
        self.ALGORITHM = ENV('ENCODE_ALGORITHM')

    """
    Creates a JWT token for the user.

    Parameters:
    - token_type: str
        + The type of token to create. It can be either 'access' or 'refresh'.
    - user: User
        + The user to create the token for.
    - return_info: bool
        + If True, the function returns the token, expiration date, and issued date.

    Returns:
    - token: str
        + The token created.
    - expires: datetime
        + The expiration date of the token.
    - issued_at: datetime
        + The date the token was issued.
    """
    def create_token(self, token_type, user, return_info=False):
        if token_type == 'access':
            key = self.TOKEN_ENCRYPTION_KEY
            expires = timezone.now() + timezone.timedelta(hours=int(ENV('TOKEN_EXPIRATION_HOURS')))
        else:
            key = self.REFRESH_ENCRYPTION_KEY
            expires = timezone.now() + timezone.timedelta(days=int(ENV('REFRESH_EXPIRATION_DAYS')))

        issued_at = timezone.now()
        token = jwt.encode({
            'user_id': user.id,
            'exp': expires,
            'iat': issued_at,
        }, key, algorithm=self.ALGORITHM)

        if return_info:
            return token, expires, issued_at
        
        return token
    

    """
    Decodes a JWT token.

    Parameters:
    - token: str
        + The token to decode.

    Returns:
    - dict
        + The decoded token.

    Raises:
    - jwt.ExpiredSignatureError
        + If the token has expired.
    - jwt.InvalidTokenError
        + If the token is invalid.
    - Exception
        + If an error occurs while decoding the token.
    """
    def decode_token(self, access_token):
        token = access_token.split(' ')[1]
        try:
            return jwt.decode(token, self.TOKEN_ENCRYPTION_KEY, algorithms=[self.ALGORITHM])
        except jwt.ExpiredSignatureError:
            return 'expired'
        except jwt.InvalidTokenError:
            return 'invalid'
        except Exception as e:
            return e
        

    """
    Decodes a JWT refresh token.

    Parameters:
    - token: str
        + The token to decode.

    Returns:
    - dict
        + The decoded token.

    Raises:
    - jwt.ExpiredSignatureError
        + If the token has expired.
    - jwt.InvalidTokenError
        + If the token is invalid.
    - Exception
        + If an error occurs while decoding the token.
    """
    def decode_refresh_token(self, token):
        try:
            return jwt.decode(token, self.REFRESH_ENCRYPTION_KEY, algorithms=[self.ALGORITHM])
        except jwt.ExpiredSignatureError:
            return 'expired'
        except jwt.InvalidTokenError:
            return 'invalid'
        except Exception as e:
            return e
        