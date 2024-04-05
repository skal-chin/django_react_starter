### Password Validation Rules

The project includes a simple password validation function that adheres to the basic rules for a secure password. The function rules are:

- must be at least 8 characters long
- must contain at least one uppercase letter
- must contain at least one lowercase letter
- must contain at least one number
- must contain at least one special character

These rules can be modified in the `passwordValidation` function in the `client/src/utils/validatePassword.js` file. It currently uses regular expressions to check for these rules.