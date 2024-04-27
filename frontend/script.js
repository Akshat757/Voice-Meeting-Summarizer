const heading = document.getElementById('moving-heading');

heading.addEventListener('mousemove', (e) => {
    const xPos = (e.clientX / window.innerWidth) * 100;
    const offset = 50 - xPos;
    heading.style.left = `${offset}px`;
});
