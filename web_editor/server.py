import os
from flask import Flask, request, jsonify, send_from_directory
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    messages = data.get("messages", [])
    markdown = data.get("markdown", "")

    system_message = {
        "role": "system",
        "content": (
            "Du er en hjelpsom assistent som redigerer markdown-tekst. "
            "Svar kun med den oppdaterte markdownen."
        ),
    }
    prompt_messages = [system_message] + messages
    prompt_messages.append({"role": "user", "content": f"Gjeldende tekst:\n{markdown}"})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt_messages,
        )
        new_markdown = response.choices[0].message["content"].strip()
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500

    return jsonify({"markdown": new_markdown})


if __name__ == "__main__":
    app.run(debug=True)
