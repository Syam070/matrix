document.addEventListener("DOMContentLoaded", function () {
    const chatDisplay = document.getElementById("chat-display");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", handleUserInput);

    function handleUserInput() {
        const userMessage = userInput.value;
        displayMessage("user", userMessage);
        userInput.value = "";

        sendMessageToBot(userMessage);
    }

    function sendMessageToBot(message) {
        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: message }),
        })
            .then((response) => response.json())
            .then((data) => {
                const botMessage = data.message;
                displayMessage("bot", botMessage);
            })
            .catch((error) => {
                console.error(error);
            });
    }

    function displayMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.className = `${sender}-message`;
        messageDiv.innerText = message;
        chatDisplay.appendChild(messageDiv);
    }
});
