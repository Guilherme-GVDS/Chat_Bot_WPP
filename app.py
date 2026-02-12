from fastapi import FastAPI, Request
from bot.ai_bot import AIBot
from services.waha import Waha
import asyncio
import random

app = FastAPI()


@app.post('/chatbot/webhook')
async def webhook(request: Request):

    data = await request.json()

    if data.get("event") != "message":
        return {"status": "ignorado"}
    if data["payload"].get("fromMe"):
        return {"status": "mensagem enviada por mim, ignorada"}
    waha = Waha()
    ai_bot = AIBot()

    chat_id = data['payload']['from']
    received_message = data['payload']['body']

    is_group = '@g.us' in chat_id
    is_status = 'status@broadcast' in chat_id

    if is_group or is_status:
        return {'mensagem': 'Mensagem de grupo ou status, ignorada.'}

    await waha.start_typing(chat_id=chat_id)
    history_messages = await waha.get_history_messages(
        chat_id=chat_id,
        limit=10)

    response_message = ai_bot.invoke(
        history_messages=history_messages,
        question=received_message)

    await asyncio.sleep(random.randint(2, 5))

    await waha.send_message(
        chat_id=chat_id,
        message=response_message
    )
    print(f'Esse é o Chat_id: {chat_id}')
    await waha.stop_typing(chat_id=chat_id)

    return {'mensagem': 'Mensagem recebida', 'data': data}
