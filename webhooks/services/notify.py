import requests
from datetime import datetime

class Notifier:

    def __init__(self):
        self.__base_url = "https://webhook.site/"

    def send_event(self) -> str:
        data = {
            "event_type": "create_outflow",
            "timestamp": datetime.now().replace(microsecond=0).isoformat(),
            "quantity": 1,
            "value": 1.75,
            "item": "keyboard"
        }

        response = requests.post(url=f"{self.__base_url}76e70a04-5d6a-48ea-85ab-9a2f78829192", json=data)
        return response.text

if __name__ == "__main__":
    notifier = Notifier()
    print(notifier.send_event())