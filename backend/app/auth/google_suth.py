from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from pathlib import Path

router = APIRouter(prefix="/auth")

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent
CREDENTIALS_DIR = BASE_DIR / "credentials"
CLIENT_SECRET_FILE = CREDENTIALS_DIR / "client_secret.json"
TOKEN_FILE = CREDENTIALS_DIR / "token.json"

SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/gmail.readonly"
]

# Redirect URI must match Google Console OAuth settings
REDIRECT_URI = "http://localhost:8000/auth/callback"

@router.get("/login")
def login():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    auth_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent"
    )
    return RedirectResponse(url=auth_url)


@router.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRET_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    flow.fetch_token(code=code)

    creds = flow.credentials

    # Save token for future use
    CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)
    with open(TOKEN_FILE, "w") as token_file:
        token_file.write(creds.to_json())

    return {"message": "Login successful and token saved!"}


def get_google_creds() -> Credentials:
    if not TOKEN_FILE.exists():
        raise Exception("No token file found. Please log in at /auth/login first.")
    return Credentials.from_authorized_user_file(str(TOKEN_FILE), scopes=SCOPES)
