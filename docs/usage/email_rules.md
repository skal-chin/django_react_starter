#### Email Validation Rules

The rules for email validation are in the utils files `validate_email.py` and `validateEmail.js` for the server and client respectively. Validation happens on both ends of the project. These files can be found in the `server/core/utils` and `client/src/utils` directories. If there are any desired deletions or additions to these rules, please make the changes in both files and refer to the list of rules below.

There are constants built into both files that can be changed to adjust the rules. The constants are as follows:

- `SPECIAL_CHARS` - A list of the special characters that are used to check for doubles in the local portion, starts and ends in the local and domain portions, and the domain portion itself.

- `ALLOWED_CHARS` - A list of the allowed special characters that can be used in the domain portion.

- `MAX_LOCAL_LENGTH` - The max length of the local portion. The current max length is 64.

- `MAX_DOMAIN_LENGTH` - The max length of the domain portion. The current max length is 255.

- `MAX_SUBDOMAIN_LENGTH` - The max length of the subdomain. The current max length is 63.

- `MAX_EMAIL_LENGTH` - The max length of the email. The current max length is 320.

General rules for email validation are as follows:

1. The email is the max length of the local portion (the part before the `@` symbol) and the domain portion (the part after the `@` symbol) combined, plus 1 for the _@_ symbol. **The current max length is 320.**

2. Cannot be empty.

3. Must contain an `@` symbol.

4. Cannot contain any spaces. Email addresses can contain spaces if they are enclosed in double quotes, but this is not supported.

Local portion rules:

1. Cannot be empty or longer than the max length of 64.

2. Cannot contain double special characters (e.g. `..`).

3. Cannot start or end in a special character.

Domain portion rules:

1. Cannot be empty or longer than the max length of 255.

2. Cannot contain a special character, except for the allowed special characters.

Subdomain rules:

1. There must be at least 2 subdomains, the domain and the top-level domain (TLD).

2. The subdomain cannot be empty or longer than the max length of 63.

3. Cannot start or end in a special character.

4. The TLD is at least 2 characters long.

These are the current rules for email validation. There are plenty of other rules that can be added, but these are the common ones. There are also REGEX patterns that can be used to validate emails, but these were written to allow for easier readability and maintainability.