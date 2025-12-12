from fastapi import FastAPI
from dotenv import load_dotenv
from app.database import engine, Base
from app.models import User
from app.routes import user_routes

load_dotenv()
app = FastAPI()
Base.metadata.create_all(engine)
app.include_router(user_routes)