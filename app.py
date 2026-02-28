from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import json
import random
from fastapi.staticfiles import StaticFiles
import asyncio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load intents file
with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

intents = data["intents"]

conversation_history = []


def get_response(user_message):
    user_message = user_message.lower().strip()

    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() == user_message:
                return random.choice(intent["responses"])

    return "Sorry, I don't understand that yet."


@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/chat", response_class=HTMLResponse)
async def chat(request: Request):
    global conversation_history

    form = await request.form()
    user_message = form.get("message")

    # simulate AI thinking time
    await asyncio.sleep(1.5)

    bot_reply = get_response(user_message)

    conversation_history.append((user_message, bot_reply))

    chat_html = ""
    for u, b in conversation_history:
        chat_html += f"<div class='user'><b>You:</b> {u}</div>"
        chat_html += f"<div class='bot'><b>Bot:</b> {b}</div>"

    return chat_html