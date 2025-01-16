// Function to toggle the mobile menu
function toggleMobileMenu() {
    const menuItems = document.querySelector('.menu-items');
    if (menuItems) {
      menuItems.classList.toggle('show');
    }
  }
  
  // Event listener for the hamburger button
  const menuToggle = document.querySelector('.menu-toggle');
  if (menuToggle) {
    menuToggle.addEventListener('click', toggleMobileMenu);
  }