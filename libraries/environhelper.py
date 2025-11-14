## ENVIRONHELPER - Helps fetch only safe environment values

import os

SAFE_ENV_KEYS = { # Define the environment variables that are safe to expose
    "LANGUAGE",
    "LIBRARY_NAME"
}

def get_safe_env(): # Returns a safe environment table for Jinja
    safe_env = {}

    for key in SAFE_ENV_KEYS:
        value = os.getenv(key)
        if value is not None:
            safe_env[key] = value

    return safe_env