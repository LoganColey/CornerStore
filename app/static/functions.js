//Sliding thingy
var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs((slideIndex += n));
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("slideshow_dot");
  if (n > x.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  for (let d = 0; d < dots.length; d++) {
    dots[d].style.color = "white";
    dots[d].style.fontSize = "200%";
  }
  x[slideIndex - 1].style.display = "block";
  var game = document.getElementById("game_name");
  game.innerText = x[slideIndex - 1].id;
  dots[slideIndex - 1].style.color = "gray";
  dots[slideIndex - 1].style.fontSize = "300%";
}

function currentDiv(n) {
  showDivs((slideIndex = n));
}