import os


# Windows cmd: "set SECRET_KEY=Very_secret_muahaha"
# Windows powershell: $env:SECRET_KEY="Very_secret_muahaha"
# Linux: export SECRET_KEY="Very_secret_muahaha"

# Note: Sometimes you need to restart the IDE or machine for the program to actually find the secret key.

class Secrets:
    SECRET_KEY = "placeholder_but_please_do_not_use_hardcoded_secrets"
    #SECRET_KEY = os.environ.get('SECRET_KEY')
