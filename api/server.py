from fastapi import FastAPI, WebSocket
from fastapi_socketio import SocketManager
from .routers import message
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["http://localhost:5173", "http://localhost:8800"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(message.router)
sio = SocketManager(app=app, cros_allowed_origins=["*"], mount_location='/')
clients = set()


@app.get('/healthcheck')
def healthcheck():
    return {"status": "ok"}


@app.sio.event
def connect(sid, environ, auth):
    print('connect ', sid)
    clients.add(sid)


@app.sio.event
def disconnect(sid):
    print('disconnect ', sid)
    clients.remove(sid)


@app.sio.on('join')
async def handle_join(sid, *args, **kwargs):
    print('join', sid, args)
    await sio.emit('broadcast_join', args)


@app.sio.on('add')
async def handle_add(sid, *args, **kwargs):
    print('add', sid, args)
    await sio.emit('broadcast_add', args)


@app.sio.on('like')
async def handle_like(sid, *args, **kwargs):
    print('like', sid)
    await sio.emit('broadcast_like', args)

# @app.websocket('/ws')
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     key = websocket.headers.get('sec-websocket-key')
#     clients[key] = websocket

#     try:
#         while True:
#             data = await websocket.receive_text()
#             for client in clients.values():
#                 await websocket.send_text(f'Message text was: {data}')

#     except:
#         await websocket.close()
#         del clients[key]
