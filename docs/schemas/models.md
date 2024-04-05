## Models

---

### User

```json
{
    "id": "string",
    "username": "string",
    "email": "string",
    "password": "string",
    "is_staff": "boolean",
    "is_active": "boolean",
    "date_joined": "string"
}
```

### Token

```json
{
    "id": "string",
    "token_type": "string",
    "token": "string",
    "expires": "DateTime",
    "issued_at": "DateTime",
    "is_valid": "boolean",
    "user": "User"
}

the token type is either "access" or "refresh"
```