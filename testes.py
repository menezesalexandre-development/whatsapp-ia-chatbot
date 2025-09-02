from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Defina sua chave de API do OpenRouter como variável de ambiente
API_KEY = "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"
if not API_KEY:
    raise ValueError("Defina a variável de ambiente OPENROUTER_API_KEY com sua chave da OpenRouter.")

# Modelo que você quer usar
MODEL_NAME = "openrouter/auto"  # você pode trocar por "meta-llama/llama-3-8b-instruct" ou outro

# Histórico de mensagens
messages = [{"role": "system", "content": "Você é um assistente útil e responde sempre em português."}]

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"error": "Nenhuma mensagem enviada"}), 400
    
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
