import requests # type: ignore
from decouple import config # type: ignore

# Send Message
def send_message(message):
  bot_token = config("TELEGRAM_TOKEN")
  chat_id = config("TELEGRAM_CHAT_ID")
  url = f"https://api.telegram.org/bot6729968180:AAG8mNRjsOpmoF9V8A3p3TEAwcZ5N6v01II/sendMessage?chat_id=6885297299&text=Moneyyyyy"
  res = requests.get(url)
  if res.status_code == 200:
    return "sent"
  else:
    return "failed"