### Email Validaton

A custom email validation function is built into the client side portion of the project. This function checks for the following rules:

- must contain only one "@" symbol
- does not contain any spaces
- is not empty or longer than 254 characters
- local portion is not longer than 64 characters
- local portion does not contain double special characters
- local portion does not start with a special character
- local portion does not end with a special character
- domain portion is not longer than 64
- domain portion does not contain special characters except for hyphens and periods
- domain portion does not start with a hyphen
- must contain a top level domain (TLD) of at least 2 characters

These rules can be modified in the `emailValidation` function in the `client/src/utils/validateEmail.js` file. The function returns an object that follows this format:

```javascript
{
  valid: true, // or false
  message: "Email is not valid" // or a custom message
}
```

These rules are very basic and not internationalized.