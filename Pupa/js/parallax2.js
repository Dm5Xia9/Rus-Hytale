let bg2 = document.querySelector('.OpBackEf2');
window.addEventListener('mousemove', function(e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;  
    bg2.style.transform = 'translate(-' + x * 20 + 'px, -' + y * 20 + 'px)';
});