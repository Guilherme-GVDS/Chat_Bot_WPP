import requests
import os
class Waha:

    def __init__(self):
        self.__api_url = 'http://waha:3000'
        self.__api_key = os.getenv("WAHA_API_KEY")

    def send_message (self, chat_id, message):
        url = f'{self.__api_url}/api/sendText'
        headers = {
            'Content-Type' : 'application/json',
            'X-API-KEY': self.__api_key
            
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
            'text': message
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers
        )

    
    def start_typing(self, chat_id):
        url = f'{self.__api_url}/api/startTyping'

        headers = {
            'Content-Type' : 'application/json'
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers
        )        


    def stop_typing(self, chat_id):
        url = f'{self.__api_url}/api/stopTyping'

        headers = {
            'Content-Type' : 'application/json'
        }
        payload = {
            'session': 'default',
            'chatId': chat_id,
        }
        requests.post(
            url=url,
            json=payload,
            headers=headers
        )        