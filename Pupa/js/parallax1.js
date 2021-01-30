let bg = document.querySelector('.OpBackEf1');
window.addEventListener('mousemove', function(e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;  
    bg.style.transform = 'translate(-' + x * 10 + 'px, -' + y * 10 + 'px)';
});
