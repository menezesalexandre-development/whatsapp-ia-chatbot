from WPP_Whatsapp import Create

# start client with your session name
your_session_name = "ProsAI"
creator = Create(session=your_session_name)
client = creator.start()
# Now scan Whatsapp Qrcode in browser

#check state of login
if creator.state != 'CONNECTED':
    raise Exception(creator.state)

def new_message(message):
    global client
    # Add your Code here
    if message and not message.get("isGroupMsg"):
        chat_id = message.get("from")
        message_id = message.get("id")
        message_body = message.get("body")
        print(message_body)

        import requests

        data = {
            'message': message_body
        }

        r = requests.post('http://127.0.0.1:5001/chat', json=data)
        json_response = r.json()
        print(json_response)
        resposta = json_response['reply']
        print(resposta)
        

        if "السلام عليكم" in message.get("body"):
            client.reply(chat_id, "وعليكم السلام", message_id)
        else:
            client.reply(chat_id, resposta, message_id)


# Add Listen To New Message
creator.client.onMessage(new_message)
