# codex

Test av OpenAI Codex

## Webbasert markdown-editor

Denne katalogen inneholder en enkel Flask-applikasjon som starter en webbasert
markdown-editor med en sidepanel som bruker ChatGPT via OpenAI sitt API. For å
kjøre serveren må du ha `OPENAI_API_KEY` satt i miljøet.

```
cd web_editor
pip install flask openai
python server.py
```

Applikasjonen blir da tilgjengelig på `http://localhost:5000`.
