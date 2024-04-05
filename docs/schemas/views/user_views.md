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
