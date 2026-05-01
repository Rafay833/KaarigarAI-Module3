from fastapi import FastAPI
from modules.m3_image.router import router as image_router

app = FastAPI(title="KaarigarAI")
app.include_router(image_router)