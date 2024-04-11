## Views

### User Views

#### register/ POST

```json

used to register a new user.

request:
{
    "email" : "EMAIL",
    "username" : "USERNAME",
    "password" : "PASSWORD"
}

returns:

{
    "id" : "ID",
    "username" : "USERNAME",
    "token" : "ACCESS_TOKEN",
    "status" : 201
}

{
    "error" : "error message",
    "status" : 400
}

The error message includes:
- "email already exists"
- "username already exists"
- "invalid email"
- "invalid password"
- "email or password is required"
```

#### login/ POST

```json

used to login a user.

request:
{
    "email" : "EMAIL",
    "password" : "PASSWORD"
}

returns:

{
    "id" : "ID",
    "username" : "USERNAME",
    "token" : "ACCESS_TOKEN",
    "status" : 200
}

{
    "error" : "error message",
    "status" : 400
}

The error message includes:
- "invalid email"
- "invalid password"
- "email or password is required"
```

#### logout/ GET

```json

uses the refresh cookie to logout a user.

returns:

{
    "message" : "logged out",
    "status" : 200
}
```

#### me/ GET
    
```json

used to retrieve the user's information.

returns:

{
    "id" : "ID",
    "username" : "USERNAME",
    "status" : 200
}
```

### Session Views

#### sessions/ GET

```json

used to retrieve a token based on the Refresh cookie.

returns:

{
    "token" : "ACCESS_TOKEN",
    "status" : 200
}
```

### Test Views

#### test_token/ GET

```json

tests the token generation by creating a fake user and using that user to create and print the token and decoded token.

returns:

{
    "message" : "token is valid",
    "status" : 200
}

```

#### test_protected/ GET

```json

tests the validity and existence of a token.

returns:
    
    {
        "message" : "protected_endpoint",
        "status" : 200
    }
    
    ```