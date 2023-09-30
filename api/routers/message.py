from fastapi import APIRouter, HTTPException
import api.schemas.message as message_schema

from ..models.message import Message
from ..message_store import MessageStore

router = APIRouter()
store = MessageStore()


@router.get('/healthcheck')
async def check():
    return {'status': 'ok'}


@router.get('/msg')
async def load():
    return {'msg', 'hello'}


@router.get('/messages', response_model=list[message_schema.Message])
def list_messages():
    return store.messages


@router.post('/messages', response_model=message_schema.MessageAddResponse)
async def add_message(message_body: message_schema.MessageAdd):
    new_msg = Message(**message_body.model_dump())
    store.add(new_msg)
    return new_msg


@router.put('/messages/{message_id}', response_model=message_schema.MessageAddResponse)
async def update_like(message_id: int):
    target = [m for m in store.messages if m.id == message_id]
    if target is None:
        raise HTTPException(status_code=404, detail='Message not found')

    return store.increment_like(message_id)


@router.delete('/messages/{message_id}', response_model=None)
async def delete_message(message_id: int):
    store.delete(message_id)
