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
});
