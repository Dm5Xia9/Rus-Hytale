let bg = document.querySelector('.OpBackEf1');
window.addEventListener('mousemove', function(e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;  
    bg.style.transform = 'translate(-' + x * 10 + 'px, -' + y * 10 + 'px)';
});
let bg2 = document.querySelector('.OpBackEf2');
window.addEventListener('mousemove', function(e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;  
    bg2.style.transform = 'translate(-' + x * 20 + 'px, -' + y * 20 + 'px)';
});
let bg3 = document.querySelector('.BackWhyEf1');
window.addEventListener('mousemove', function(e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;  
    bg3.style.transform = 'translate(-' + x * 10 + 'px, -' + y * 10 + 'px)';
});
let bg4 = document.querySelector('.BackWhyEf2');
window.addEventListener('mousemove', function(e) {
    let x = e.clientX / window.innerWidth;
    let y = e.clientY / window.innerHeight;  
    bg4.style.transform = 'translate(-' + x * 20 + 'px, -' + y * 20 + 'px)';
});