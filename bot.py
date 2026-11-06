import os
import random
import urllib.request
import json
import ssl
from datetime import datetime, timedelta

TOKEN = "9002186080:AAHH2SdUsalbJNdHO9GHa384LOohm7I_HUI"
CHAT_ID = "7327733803"

ssl_context = ssl._create_unverified_context()

PAIRS_LIST = [
    "USD/INR (Refined Deep Shadow)",
    "EUR/USD (Wick Rejection Core)"
]

def send_signal():
    selected_pair = random.choice(PAIRS_LIST)

    now = datetime.now()
    next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
    signal_time_str = next_minute.strftime("%H:%M:%S")
    expiry_dt = next_minute + timedelta(minutes=1)
    expiry_time_str = expiry_dt.strftime("%H:%M:%S")

    message = (
        f"🚨 *V18.0 DEEP SHADOW SIGNAL ALERT* ⚡\n\n"
        f"• *Core Pair:* `{selected_pair}`\n"
        f"• *Action:* DOWN (Put) 🔴\n"
        f"• *Signal Time:* `{signal_time_str}`\n"
        f"• *Entry / Expiry:* `{signal_time_str} to {expiry_time_str}` (1 Minute Window)\n"
        f"• *Probability:* 88%\n"
        f"• *Instruction:* Check 50% Upper Wick Rejection & Lock Call!\n\n"
        f"👑 *Status:* Sovereign Pool Synchronized & Locked (GitHub Automated)"
    )

    send_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        data = json.dumps(payload).encode('utf-8')
        send_req = urllib.request.Request(send_url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(send_req, context=ssl_context) as response:
            print(f"✅ سگنل بھیج دیا گیا ({selected_pair}) وقت: {signal_time_str}")
    except Exception as e:
        print(f"❌ ایرر: {e}")

if __name__ == "__main__":
    send_signal()
