import re
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from main import *

app = FastAPI()

#@app.get("/getChatBotResponse")
#def get_bot_response(msg: str):
#    res = get_response(msg)
#    return str(res)

@app.get("/getChatBotResponse")
async def get(data: str):
    res = get_response(data)
    return str(res)

@app.websocket("/getChatBotResponse")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text(websocket)
        await websocket.send_text(data)
 #       return str(data)