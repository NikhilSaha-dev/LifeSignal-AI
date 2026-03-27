function sendMessage() {
    let inputField = document.getElementById("userInput");
    let message = inputField.value;

    if (message.trim() === "") return;

    let chatbox = document.getElementById("chatbox");

    // User message
    chatbox.innerHTML += `<div class="user-msg">${message}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        chatbox.innerHTML += `<div class="ai-msg">${data.reply}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    inputField.value = "";
}