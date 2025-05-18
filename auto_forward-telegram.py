from flask import Flask, render_template_string, request
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio

# API config
api_id = 19671790
api_hash = '987fea1ede441e22fb549d7a215ea921'
session_name = 'session'

# Flask app
app = Flask(__name__)

# HTML Template (modern style)
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Telegram Auto Forwarder</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #f0f2f5; text-align: center; padding: 30px; }
        form { background: white; padding: 30px; border-radius: 12px; display: inline-block; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; border-radius: 8px; border: 1px solid #ccc; }
        button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer; transition: 0.3s; }
        button:hover { background: #0056b3; }
        .msg { margin-top: 20px; font-weight: bold; color: green; }
    </style>
</head>
<body>
    <h2>Telegram Auto Forwarder</h2>
    <form method="POST">
        <input name="source_chat" placeholder="Source Chat ID (e.g. -1001234567890)" required>
        <input name="message_id" placeholder="Message ID" required>
        <textarea name="targets" rows="6" placeholder="Target usernames, one per line (without @)" required></textarea>
        <button type="submit">Start Forwarding</button>
    </form>
    {% if result %}
        <div class="msg">{{ result }}</div>
    {% endif %}
</body>
</html>
"""

# Async forwarding function
async def forward_messages(source_chat, message_id, targets):
    async with TelegramClient(session_name, api_id, api_hash) as client:
        if not await client.is_user_authorized():
            await client.send_code_request(phone=input("Enter your phone number: "))
            try:
                await client.sign_in(code=input("Enter the code: "))
            except SessionPasswordNeededError:
                await client.sign_in(password=input("2FA Password: "))

        success = 0
        fail = 0
        for username in targets:
            try:
                await client.forward_messages(username.strip(), message_id=int(message_id), from_peer=int(source_chat))
                print(f"[+] Forwarded to: {username}")
                success += 1
                await asyncio.sleep(5)
            except Exception as e:
                print(f"[-] Failed to {username}: {e}")
                fail += 1
        return f"Done! Success: {success}, Failed: {fail}"

# Route
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        source_chat = request.form["source_chat"]
        message_id = request.form["message_id"]
        targets = request.form["targets"].splitlines()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(forward_messages(source_chat, message_id, targets))
    return render_template_string(html_template, result=result)

# Run app
if __name__ == "__main__":
    app.run(debug=True)