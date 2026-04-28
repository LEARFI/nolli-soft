from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

# Vercel ищет именно переменную с именем "app"
app = FastAPI() 

templates = Jinja2Templates(directory="templates")

# Данные от Телеграм
API_ID = '38989690'
API_HASH = '0b765d2f53175c9b24abc29c4511080e'

@app.get("/")
async def home(request: Request):
    # Оставляем только одну версию функции. 
    # Все данные для страницы (контекст) передаем в одном словаре.
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"your_context_key": "value"}
    )

# Сюда дописываешь свои функции для работы с Telegram
