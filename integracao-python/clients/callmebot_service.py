import requests
import os
from dotenv import load_dotenv

load_dotenv()

class CallMeBot:
    def __init__(self):
        self.__cell_phone = os.getenv("NUMBER")
        self.__base_url = f"https://api.callmebot.com/whatsapp.php?phone={self.__cell_phone}&text="
        self.__api_key = os.getenv("CALLMEBOT_API_KEY")

    def send_message(self, message):
        reponse = requests.get(
            url=f"{self.__base_url}{message}&apikey={self.__api_key}")
        return reponse.text
