from fastapi import FastAPI , Response
from routers.upload import router as upload_router
from routers.ask import router as ask_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app =FastAPI()

app.include_router(ask_router)
app.include_router(upload_router)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)