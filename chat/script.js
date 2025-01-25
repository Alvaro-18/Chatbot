document.querySelector("form").addEventListener("submit", function (event) {
  event.preventDefault();  
});

document.getElementById("sendBtn").addEventListener("click", function () {
  const input = document.getElementById("question");
  const userMessage = input.value;

  if (userMessage.trim() !== "") {
    displayMessage(userMessage, "user");

    fetch(`http://localhost:5000/resposta/${userMessage.toLowerCase()}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    }).then(response => response.json())
      .then(data => {
        console.log(data.resposta);
        displayMessage(data.resposta, "bot");
      })
      .catch(error => {
        console.error("Erro ao buscar resposta do bot:", error);
      });

    input.value = ""; 
  }
});

function displayMessage(message, sender) {
  const messageDiv = document.createElement("li");
  messageDiv.classList.add("message");

  if (sender === "user") {
    messageDiv.classList.add("question");
  } else {
    messageDiv.classList.add("response");
  }

  messageDiv.textContent = message;

  const messagesContainer = document.getElementById("messagesContainer");
  messagesContainer.appendChild(messageDiv);

  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
