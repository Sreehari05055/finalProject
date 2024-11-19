
    window.onload = function() {
    const chatBox = document.getElementById('chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
};

function scrollToBottom() {
    const chatBox = document.getElementById('chat-box');
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

    function toggleDropdown() {
            var dropdown = document.getElementById("dropdownMenu");
            dropdown.classList.toggle("is-active");
        }

        // Close the dropdown if the user clicks outside of it
        window.onclick = function(event) {
             const dropdownMenu = document.getElementById("dropdownMenu");
             const profileIcon = document.querySelector(".profile-icon");

    // If the click is outside the dropdown and profile icon, close the dropdown
    if (!dropdownMenu.contains(event.target) && !profileIcon.contains(event.target)) {
        dropdownMenu.classList.remove("is-active");
    }
};

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
