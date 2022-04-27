const foodbox = document.getElementById("content");
const ticketDisplay = document.getElementById("ticketDisplay");
const options = document.querySelectorAll(".Btn");
let total = 0;
const totalText = document.getElementById("total");
var dt = new Date();
const sidesNames = [];

function checkDateTime() {
  if (dt.getDay() != 5 && dt.getDay() != 6) {
    document.getElementById("myDropdown").insertAdjacentHTML(
      "beforeend",
      `
        <a class="Btn" name="seafood" href="{% url 'sortmenu' "seafood" %}">Seafood</a>
      `
    );
  }
}

//toggle menu
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
