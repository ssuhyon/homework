document.addEventListener('DOMContentLoaded', function() {
    const likeButton = document.getElementById('like-button');
    if (likeButton) {
        likeButton.addEventListener('click', function() {
            fetch(likeButton.dataset.url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': likeButton.dataset.csrf,
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('like-count').textContent = data.likes;
            });
        });
    }
});