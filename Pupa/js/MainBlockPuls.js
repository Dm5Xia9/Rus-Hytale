function createRipple1(event) {
    const button = event.currentTarget;
  
    const circle = document.createElement("span");
    const diameter = Math.max(200, 200);
    const radius = diameter / 2;
  
    circle.style.width = circle.style.height = `${diameter}px`;
    circle.style.left = `${event.clientX - button.offsetLeft - radius}px`;
    circle.style.top = `${event.clientY - button.offsetTop - radius}px`;
    circle.classList.add("ripple1");
  
    const ripple = button.getElementsByClassName("ripple1")[0];
  
    if (ripple) {
      ripple.remove();
    }
  
    button.appendChild(circle);
  }
  
  const buttons1 = document.getElementsByClassName("imgMainBlock");
  for (const button of buttons1) {
    button.addEventListener("click", createRipple1);
    
  }