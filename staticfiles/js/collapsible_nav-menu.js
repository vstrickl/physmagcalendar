// Function to toggle the mobile menu
function toggleMobileMenu() {
    const menuItems = document.querySelector('.menu-items');
    menuItems.classList.toggle('show');
  }
  
  // Event listener for the hamburger button
  const menuToggle = document.querySelector('.menu-toggle');
  menuToggle.addEventListener('click', toggleMobileMenu);