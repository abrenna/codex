async function sendMessage(content) {
    const textarea = document.getElementById('markdown');
    const markdown = textarea.value;

    const messages = window.chatHistory || [];
    messages.push({ role: 'user', content });

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages, markdown })
    });

    const data = await response.json();
    if (data.markdown) {
        textarea.value = data.markdown;
        addMessage('assistant', data.markdown);
    } else if (data.error) {
        addMessage('assistant', 'Feil: ' + data.error);
    }

    window.chatHistory = messages;
}

function addMessage(role, text) {
    const messagesDiv = document.getElementById('messages');
    const div = document.createElement('div');
    div.className = role;
    div.textContent = text;
    messagesDiv.appendChild(div);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

document.getElementById('chat-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const input = document.getElementById('chat-input');
    const text = input.value.trim();
    if (text) {
        addMessage('user', text);
        sendMessage(text);
        input.value = '';
    }
});
