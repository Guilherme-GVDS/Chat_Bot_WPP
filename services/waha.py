import os
import httpx


class Waha:

    def __init__(self):
        self.__api_url = 'http://waha:3000'
        self.__api_key = os.getenv("WAHA_API_KEY")
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.__api_key
            }

    async def send_message(self, chat_id, message):
        url = f'{self.__api_url}/api/sendText'

        payload = {
            'session': 'default',
            'chatId': chat_id,
            'text': message
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                url=url,
                json=payload,
                headers=self.headers)
        print('Mensagem Enviada: ', response.status_code, message)

    async def start_typing(self, chat_id):
        url = f'{self.__api_url}/api/startTyping'

        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                url=url,
                json=payload,
                headers=self.headers)
        print('Start_Typing: ', response.status_code)

    async def get_history_messages(self, chat_id, limit):
        url = f'{self.__api_url}/api/default/chats/{chat_id}/messages?limit={limit}&downloadMedia=false'

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                url=url)
        data = response.json()

        return data.get("data", [])

    async def stop_typing(self, chat_id):
        url = f'{self.__api_url}/api/stopTyping'

        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                url=url,
                json=payload,
                headers=self.headers)
        print('Stop_Typing: ', response.status_code)
