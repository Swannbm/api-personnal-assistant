from os import environ

PORT = int(environ.get("PORT", "8000"))
VERIFY_TOKEN = environ.get("VERIFY_TOKEN", "HAPPY")
