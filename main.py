from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from telethon import TelegramClient
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Данные от Телеграм (вставлять сюда)
API_ID = '38989690'
API_HASH = '0b765d2f53175c9b24abc29c4511080e'

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Сюда дописываешь функции парсинга и спама из примера выше
