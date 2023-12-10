from google_auth_oauthlib.flow import InstalledAppFlow

from .config import *

def request_creds():
    client_config={"web":{"client_id":CLIENT_ID,"project_id":PROJECT_ID,"auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":CLIENT_SECRET,"redirect_uris":[REDIRECT_URI],"javascript_origins":["http://localhost:8000"]}}
    flow = InstalledAppFlow.from_client_config(
        client_config,
        scopes=['email openid profile'],
    ) 
    creds = flow.run_local_server(port=0)

    return creds