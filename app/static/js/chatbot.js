document.getElementById('sendButton').addEventListener('click', function() {
    const question = document.getElementById('messageInput').value;
    const button = document.getElementById('sendButton');
    button.disabled = true;  // Deactivate  button to delete multiples clics

    fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: question }),
    })
    .then(response => response.json())
    .then(data => {
        const messagesDiv = document.getElementById('messages');
        messagesDiv.innerHTML += `<p><strong>You:</strong> ${data.question}</p>`;
        messagesDiv.innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
        button.disabled = false;  // Reactivate  button after answer
    });
});

