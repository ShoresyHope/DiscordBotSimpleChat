
import random

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'I hate you'

    if p_message == 'spanish inquistion':
        return 'was a good thing'

    if p_message == 'roll':
        return str(random.randint(1,999))

    if p_message == 'help':
        return "This is a help message that you can modify."
