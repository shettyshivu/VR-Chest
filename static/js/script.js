const hamburger = document.querySelector('.headers .nav-bars .nav-lists .hamburger');
const mobile_menu = document.querySelector('.headers .nav-bars .nav-lists ul');
const menu_item = document.querySelectorAll('.headers .nav-bars .nav-lists ul li a');
const header = document.querySelector('.headers.containers');

hamburger.addEventListener('click', () => {
	hamburger.classList.toggle('active');
	mobile_menu.classList.toggle('active');
});

document.addEventListener('scroll', () => {
	var scroll_position = window.scrollY;
	if (scroll_position > 50) {
		header.style.backgroundColor = '#17a2c2';
	} else {
		header.style.backgroundColor = 'transparent';
	}
});

menu_item.forEach((item) => {
	item.addEventListener('click', () => {
		hamburger.classList.toggle('active');
		mobile_menu.classList.toggle('active');
	});
});