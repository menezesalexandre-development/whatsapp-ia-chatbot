from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

model_name = 'dolphin-phi'
messages = [{"role": "system", "content": "You are a helpful assistant."}]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "Nenhuma mensagem enviada"}), 400
    
    # Adiciona a mensagem do usuário
    messages.append({"role": "user", "content": user_input})
    
    # Chama a IA
    response = ollama.chat(model=model_name, messages=messages)
    answer = response.message.content
    
    # Adiciona resposta ao histórico
    messages.append({"role": "assistant", "content": answer})
    
    return jsonify({"reply": answer})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    # pega o texto enviado do index.js
    user_message = data.get("message", "")

    # aqui você coloca sua lógica de IA ou resposta
    bot_response = f"Você disse: {user_message}"

    # devolve a resposta em JSON para o index.js
    return jsonify({"reply": bot_response})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
