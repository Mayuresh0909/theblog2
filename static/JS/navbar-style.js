/*const sections=document.querySelector("section");
const brandimg = document.querySelector("#inside-navbar-brand")
//const mainmenu=document.querySelector("#Main-Menu")
//const hiddenmenu = document.querySelector("#Main-Menu-scrolled")
const options={
  threshold:0.45,
  root:null
}
const observer= new IntersectionObserver(function (entries,observer) {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      brandimg.classList.remove("d-none")
      console.log(entry);
    }
    else {
    brandimg.classList.add("d-none")
    }
  });

},options);
observer.observe(sections);*/
window.addEventListener("scroll",function () {
  const header=document.querySelector("#inside-navbar-brand");
  const mainmenu=document.querySelector("#MenuBar")
  if(window.scrollY>150){
  header.classList.remove('d-lg-none')
  header.classList.add('inside-navbar-brand')
  mainmenu.classList.add('navbaranim')
  }
  else{
    header.classList.add('d-lg-none')
    mainmenu.classList.remove('navbaranim')
  }
});
$(document).ready(function () {
  $(".navbar-toggler").on("click",function () {
    $(".mobileMenu").toggleClass("open");
    $("#navbutton").toggleClass("d-none")
    //$("#closebutton").toggleClass("d-none")
  });
  $('#navbarDropdownMenuNonTech').on("click",function () {
    $("#megamenu").toggleClass("d-none");
  });
  $("#closebutton").on("click",function () {
    $(".mobileMenu").toggleClass("open");
    $("#navbutton").toggleClass("d-none");
  });
  $("#sportsbutton").on("click",function () {
    $("#sportsubmenu").toggleClass("d-none");
  })
  $('.owl-carousel').owlCarousel({
      loop:true,
      margin:10,
      nav:true,
      responsive:{
          0:{
              items:1
          },
          768:{
              items:2
          },
          992:{
              items:3
          }
      }
  })
});

AOS.init({
  duration:1000,
  offset:200
});
