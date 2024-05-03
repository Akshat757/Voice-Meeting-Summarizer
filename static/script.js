document.addEventListener('DOMContentLoaded', function() {
    const heading = document.getElementById('moving-heading');
    
    if (heading) {
        heading.addEventListener('mousemove', (e) => {
            const xPos = (e.clientX / window.innerWidth) * 100;
            const offset = 50 - xPos;
            heading.style.left = `${offset}px`;
        });
    } else {
        console.error("Element with ID 'moving-heading' not found.");
    }
});


document.getElementById("send-mail").addEventListener("click", function() {
    // Fetch the last recorded ID from the server
    fetch('/last_recorded_id')
    .then(response => response.json())
    .then(data => {
        // Set the value of the input field to the last recorded ID
        document.getElementById("select-id").value = data.last_recorded_id;
    })
    .catch(error => console.error('Error fetching last recorded ID:', error));
});