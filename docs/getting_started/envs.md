### Setting up your .envs

There are two separate .env files for this project: The client and the server. Example .envs are given in the root directory, but these files should be placed in the client and server directory, respectively, to work. You can copy the .env.example file and rename it to .env. The .env file should not be committed to the repository. It is used to store sensitive information such as API keys and database passwords.

In the server .env file, you will need to set the following variables:
SUPER_USER
PASSWORD
SERVER_SECRET_KEY
DEBUG

TOKEN_ENCRYPTION_KEY
REFRESH_ENCRYPTION_KEY
ENCODE_ALGORITHM
TOKEN_EXPIRATION_HOURS
REFRESH_EXPIRATION_DAYS

The secret key is used in the settings.py file to provide encryption.
The token encryption and the refresh encryption keys are used in the app's token generation. You should use seperate keys for these three variables. You can use [randomkeygen.com](https://randomkeygen.com/) to generate a secret key.

Use integers for the expiration times. The token expiration time is in hours and the refresh expiration time is in days.

The client .env file is used to store the API URL. You will need to set the following variable:
REACT_APP_API_URL

This is the URL that the client will use to make requests to the server. It should be set to the URL of the server. For development, it will be [http://localhost:8000](http://localhost:8000).