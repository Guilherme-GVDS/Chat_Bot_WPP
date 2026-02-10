from fastapi import FastAPI, APIRouter, Request

app = FastAPI()


@app.post('/chatbot/webhook')
async def webhook(request: Request):
    data = await request.json()
    print(f'Mensagem recebida: {data}')
    return {'mensagem': f'Mensagem recebida', 'data': data}
