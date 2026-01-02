import requests, time, os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

while True:
    r = requests.get("http://localhost:8080/location").json()
    if r:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendLocation",
            data={"chat_id": CHAT_ID,
                  "latitude": r["latitude"],
                  "longitude": r["longitude"]}
        )
    time.sleep(60)
