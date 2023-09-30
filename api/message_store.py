import itertools
from .models.message import Message


class MessageStore:
    id_obj = itertools.count()

    def __init__(self, messages: list[Message] = []):
        self.messages: list[Message] = messages

    def add(self, message: Message):
        id = next(MessageStore.id_obj)
        message.id = id
        self.messages.append(message)

    def increment_like(self, id: int):
        for (i, msg) in enumerate(self.messages):
            if msg.id == id:
                self.messages[i].like += 1
                return self.messages[i]

        return

    def delete(self, id: int):
        messages = [m for m in self.messages if m.id != id]
        if len(messages) == len(self.messages):
            print('not found')
            return

        self.messages = messages
