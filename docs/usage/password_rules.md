#### Password Validation Rules

The rules for password validation are in the utils files `validate_password.py` and `validatePassword.js` for the server and client respectively. Validation happens on both ends of the project. These files can be found in the `server/core/utils` and `client/src/utils` directories. If there are any desired deletions or additions to these rules, please make the changes in both files and refer to the list of rules below.

Regular expressions are used to validate the password. They are used here, because they are simpler to read and maintain in this instance. The expressions are held in constants on both the server and client side. The constants are as follows:

- `UPPER_REGEX` - A regular expression that checks for at least one uppercase letter.

- `LOWER_REGEX` - A regular expression that checks for at least one lowercase letter.

- `DIGIT_REGEX` - A regular expression that checks for at least one digit.

- `SPECIAL_REGEX` - A regular expression that checks for at least one special character.

The rules for password validation are as follows:

1. The password must be at least 8 characters long.

2. The password must contain at least one uppercase letter.

3. The password must contain at least one lowercase letter.

4. The password must contain at least one digit.

5. The password must contain at least one special character.