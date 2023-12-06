from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth, OAuthError
from app.config import CLIENT_ID, CLIENT_SECRET
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="add any string...")
# app.mount("/static", StaticFiles(directory="static"), name="static")

oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    client_kwargs={
        'scope': 'email openid profile',
        'redirect_url': 'http://localhost:8000/auth'
    }
)




@app.get("/")
def index(request: Request):
    user = request.session.get('user')
    print(user)
    if user:
        return RedirectResponse('welcome')

    # return templates.TemplateResponse(
    #     name="home.html",
    #     context={"request": request}
    # )


# @app.get('/welcome')
# def welcome(request: Request):
#     user = request.session.get('user')
#     print(user)
#     if not user:
#         return RedirectResponse('/')
#     return {"message":"welcome"}
 
@app.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url, prompt='select_account')


@app.get('/auth')
async def auth(request: Request):
    try:
        token = await oauth.google.authorize_access_token(request)
    except Exception as e:
        return e
    user = token.get('userinfo')
    print(user)  # Add this line to check the user data
    if user:
        request.session['user'] = dict(user)
    return RedirectResponse('welcome')


@app.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    return RedirectResponse('/')
