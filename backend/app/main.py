from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp.controller import router as mcp_router
from app.auth.google_suth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] for all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(mcp_router)