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

