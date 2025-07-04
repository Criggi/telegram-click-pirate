import time
import random
import requests

# Telegram Bot Token and Channel
BOT_TOKEN = "7617719571:AAGm1nlFVlrAPfhUAjp4Dcq1RG9kotrHz-o"
CHANNEL = "@YourGonnaWantThis"

# Amazon product IDs (mock examples — you can expand this list)
PRODUCT_IDS = [
    "B08J5QJBN2", "B07FZ8S74R", "B09F3QG2KZ", "B08N5WRWNW", "B0B3CP98ZT"
]

HOOKS = [
    "You won’t believe what this does…",
    "🔥 This item blew my mind.",
    "How is this even legal to sell?",
    "Amazon’s best kept secret is finally out!",
    "This is what everyone’s getting before it sells out 🔥"
]

def generate_post():
    product_id = random.choice(PRODUCT_IDS)
    hook = random.choice(HOOKS)
    url = f"https://www.amazon.com/dp/{product_id}/?tag=criggi92-20"
    message = f"🚨 {hook}\\n\\n👉 [Check it out on Amazon]({url})"
    return message

def post_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=payload)
    print(response.status_code, response.text)

if __name__ == "__main__":
    msg = generate_post()
    post_to_telegram(msg)
