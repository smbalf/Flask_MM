"""
Authomatic OAuth configuration file

Pull secret ids and keys from environment variables set in .env
"""

import os

from authomatic import Authomatic
from authomatic.providers import oauth2

OAUTH_CONFIG = {
    "Google": {
        "id": 1,  # These id numbers are arbitrary
        "class_": oauth2.Google,
        "consumer_key": os.getenv("GOOGLE_ID"),
        "consumer_secret": os.getenv("GOOGLE_SECRET"),
        # Google requires a scope be specified to work properly
        "scope": ["profile", "email"],
    }
}

# Instantiate Authomatic.
authomatic = Authomatic(
    OAUTH_CONFIG,
    os.getenv("AUTHOMATIC_SECRET"),
    report_errors=True,  # Set to False in production
)