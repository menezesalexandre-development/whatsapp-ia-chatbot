from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Defina sua chave de API do OpenRouter como variável de ambiente
API_KEY = "SUA_CHAVE_API"
if not API_KEY:
    raise ValueError("Defina a variável de ambiente OPENROUTER_API_KEY com sua chave da OpenRouter.")

# Modelo que você quer usar
MODEL_NAME = "openrouter/auto"  # você pode trocar por "meta-llama/llama-3-8b-instruct" ou outro

# Armazena histórico separado por usuário
conversations = {}

def get_conversation(user_id):
    if user_id not in conversations:
        conversations[user_id] = [
            {"role": "system", "content": "Você é um assistente útil e responde sempre em português."}
        ]
    return conversations[user_id]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    user_id = request.json.get("user_id", "default_user")

    if not user_input:
        return jsonify({"error": "Nenhuma mensagem enviada"}), 400
    
    messages = get_conversation(user_id)

    # Adiciona a mensagem do usuário
    messages.append({"role": "user", "content": user_input})

    # Faz a requisição para a API do OpenRouter
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL_NAME,
            "messages": messages
        }
    )

    if response.status_code != 200:
        return jsonify({"error": f"Erro na API: {response.text}"}), 500
    
    data = response.json()
    answer = data["choices"][0]["message"]["content"]

    # Adiciona resposta ao histórico
    messages.append({"role": "assistant", "content": answer})

    return jsonify({"reply": answer})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
