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




// slider

var s= document.getElementById("slideImg");
var images = new Array (
	"https://cdn-endpoint-afib.azureedge.net/afibmatters/2020/01/iStock-171372917-1536x1024.jpg",
	"https://www.babycenter.com/ims/2015/03/78751269_wide.jpg",
	"https://wallpapercave.com/wp/wp6681966.png"
);

var len = images.length;
var i =1;
 function slider()
 {
	if(i>len-1)
	{
		i=0;
	}
	s.src=images[i];
	i++;
	setTimeout('slider()',3000)
 }


 //counter
 const counters = document.querySelectorAll(".counter");

 counters.forEach((counter) => {
   counter.innerText = "0";
   const updateCounter = () => {
	 const target = +counter.getAttribute("data-target");
	 const count = +counter.innerText;
	 const increment = target / 200;
	 if (count < target) {
	   counter.innerText = `${Math.ceil(count + increment)}`;
	   setTimeout(updateCounter, 1);
	 } else counter.innerText = target;
   };
   updateCounter();
 });
 


 
  
