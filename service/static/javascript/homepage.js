     const submitButton = document.getElementById('submit-btn');
     const chatForm = document.getElementById('chat-form')
     const chatBox = document.getElementById('chat-box');

    window.onload = function() {
    chatBox.scrollTop = chatBox.scrollHeight;
};

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

        // Show the submit button only if there's input in the field
        if (inputField.value.trim() !== "") {
            submitButton.style.opacity = "1";
            submitButton.style.visibility = "visible";
            submitButton.disabled = false;
        } else {
            submitButton.style.opacity = "0";
            submitButton.style.visibility = "hidden";
            submitButton.disabled = true;
        }
    }

     chatForm.addEventListener('submit', function(event) {
      if(submitButton.disabled) {
       event.preventDefault(); // Prevent multiple submissions
        return;
      }
        submitButton.disabled = true;
        submitButton.style.opacity = "0.5";

});

function toggleClearButton()
{
    const clearFormButton = document.getElementById("clear-form");

    if (chatBox.innerHTML.trim() !== "")
    {
        clearFormButton.style.opacity = "1";
        clearFormButton.style.visibility = "visible";
    }
    else
    {
            clearFormButton.style.opacity = "0";
            clearFormButton.style.visibility = "hidden";
    }
}

toggleClearButton();