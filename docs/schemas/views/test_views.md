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