from fastapi import FastAPI, APIRouter, Request
from bot.ai_bot import AIBot
from services.waha import Waha
import time
import random

app = FastAPI()


@app.post('/chatbot/webhook')
async def webhook(request: Request):

    data = await request.json() 
    print(f'Mensagem recebida: {data}')

    waha = Waha()
    ai_bot = AIBot()

    chat_id = data['payload']['from']
    #print (f'Esse é o Chat_ID{chat_id}')
    received_message = data['payload']['body']

    waha.start_typing(chat_id=chat_id)

    response = ai_bot.invoke(question=received_message)
    #print (f'Resposta da IA: {response}')
    waha.send_message(
        chat_id=chat_id,
        message=response
    )
    waha.stop_typing(chat_id=chat_id)

    return {'mensagem': f'Mensagem recebida', 'data': data}
