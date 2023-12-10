from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
from app.config import CLIENT_ID, CLIENT_SECRET
from fastapi.staticfiles import StaticFiles
from app.creds_handler import request_creds

app = FastAPI()

request_creds()




@app.get("/")
def index():
    return {"message":"ok"}


 
