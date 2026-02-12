from fastapi import FastAPI, Request
from bot.ai_bot import AIBot
from services.waha import Waha
import asyncio
import random

app = FastAPI()


@app.post('/chatbot/webhook')
async def webhook(request: Request):

    data = await request.json()
    # print(f'Mensagem recebida: {data}')

    waha = Waha()
    ai_bot = AIBot()

    chat_id = data['payload']['from']
    received_message = data['payload']['body']

    await waha.start_typing(chat_id=chat_id)
    await asyncio.sleep(random.randint(2, 5))
    response = ai_bot.invoke(question=received_message)

    await waha.send_message(
        chat_id=chat_id,
        message=response
    )
    await waha.stop_typing(chat_id=chat_id)

    return {'mensagem': 'Mensagem recebida', 'data': data}
