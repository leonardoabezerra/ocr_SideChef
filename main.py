import sys

from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import UploadFile

from typing import Annotated, BinaryIO
from pydantic import BaseModel, FilePath

# Util Functions
def save_img(image: BinaryIO):
    content = image.read()
    with open('imgs/b.png', 'wb') as f:
        f.write(content)

# Image Router
router = APIRouter()

@router.post('/image')
async def send_image(f: UploadFile):
    save_img(f.file)

# Main
app = FastAPI()
app.include_router(router)

@app.get('/')
async def root():
    return {"message" : "Hello World!"}