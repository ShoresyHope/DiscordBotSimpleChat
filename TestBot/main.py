import bot
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import handle_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# STEP 1: BOT SETUP

intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# STEP @ MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

        try:
            response: str = handle_response(user_message)
            await message.author.send(response) if is_private else message.channel.send(response)
        except Exception as e:
            print('(Message was')