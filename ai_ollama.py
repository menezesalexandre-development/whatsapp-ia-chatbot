from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)

model_name = 'mistral'
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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
