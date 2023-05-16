import random
if __name__ == '__main__':
    pass
def handle_response(message)->str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hello there'
    if p_message == 'roll':
        return str(random.randint(1,10))
    if p_message == 'help':
        return "`Help`"
    return "I am not sure I understand"
