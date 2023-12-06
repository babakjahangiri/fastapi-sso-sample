from authlib.integrations.starlette_client import OAuth
from .config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI

oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs={
        'scope': 'email openid profile',
        'redirect_url': REDIRECT_URI,
    }
)