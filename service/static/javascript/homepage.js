    const chatBox = document.getElementById('chat-box');

function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

    document.getElementById('clear-form').addEventListener('submit', function(event) {
        event.preventDefault();

        fetch(clearChatUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            credentials: 'same-origin'
        })
        .then(response => {
            if (response.ok) {
               const chatBubbles = document.querySelectorAll('.chat-bubble');
                chatBubbles.forEach(bubble => {
                    bubble.remove();  // This will remove each chat bubble
                });
            }
        });
    });

        function toggleSubmitButton() {
        const inputField = document.getElementById('question');
        const submitButton = document.getElementById('submit-btn');

        // Show the submit button only if there's input in the field
        if (inputField.value.trim() !== "") {
            submitButton.style.opacity = "1";
            submitButton.style.visibility = "visible";
        } else {
            submitButton.style.opacity = "0";
            submitButton.style.visibility = "hidden";
        }
    }