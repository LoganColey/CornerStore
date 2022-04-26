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

// fetch("/static/food.json")
//   .then((req) => req.json())
//   .then((data) => {
//     console.log(data);
//     for (const item of data) {
//       if (item.type == "side") {
//         sidesNames.push(item.name);
//       }
//     }
//   });

// //makes menu dropdown buttons work
// options.forEach((m) => {
//   m.addEventListener("click", (e) => {
//     if (e.target.innerHTML === "Burgers and More") {
//       foodbox.innerHTML = "";
//       fetchingAndPopulating("small", "Burgers and More");
//     } else if (e.target.innerHTML === "Sides") {
//       foodbox.innerHTML = "";
//       fetchingAndPopulating("side", "Sides");
//     } else if (e.target.innerHTML === "Plates") {
//       foodbox.innerHTML = "";
//       fetchingAndPopulating("big", "Plates");
//     } else if (e.target.innerHTML === "Salads") {
//       foodbox.innerHTML = "";
//       fetchingAndPopulating("salad", "Salads");
//     } else if (e.target.innerHTML === "Starters") {
//       foodbox.innerHTML = "";
//       fetchingAndPopulating("starter", "Starters");
//     } else if (e.target.innerHTML === "Seafood") {
//       foodbox.innerHTML = "";
//       fetchingAndPopulating("seafood", "Seafood");
//     }
//   });
// });

// function removeItem(event) {
//   var button = event.target;
//   var item_card = button.parentElement;
//   var item_price = item_card
//     .getElementsByClassName("item-price")[0]
//     .innerText.substring(1);
//   total -= Number(item_price);
//   totalText.innerHTML = "";
//   if (total <= 0) {
//     document.querySelector(".checkoutbtn").classList.remove("show");
//     totalText.innerHTML = "$0.00";
//   } else {
//     totalText.innerHTML = "$" + total.toFixed(2);
//   }
//   button.parentElement.parentElement.remove();
// }

function openCheckout() {
  //see if all sides are chosen
  if (document.querySelectorAll(".sideDrop").length > 0) {
    var missing = false;
    for (const sideDrop of document.querySelectorAll(".sideDrop")) {
      if (sideDrop.options[sideDrop.selectedIndex].value == 0) {
        missing = true;
      }
    }
    if (missing == true) {
      document.querySelector(".sidesError").classList.add("show");
      //if side is loaded baked potato or side salad, add $2.50 to total
    } else {
      document.querySelector(".sidesError").classList.remove("show");
      displayCheckout();
    }
  } else {
    document.querySelector(".sidesError").classList.remove("show");
    displayCheckout();
  }
}

function ticketToggle() {
  //   if (dt.getHours() * 100 + dt.getMinutes() >= 1630 && dt.getHours() < 19) {
  //     document.getElementById("ticketSide").classList.toggle("show");
  //     document.querySelector(".mainpage").classList.toggle("grid");
  //     document.getElementById("total").classList.toggle("show");
  //   } else {
  //     document.querySelector(".afterHoursError").classList.toggle("show");
  //   }
  // }

  document.getElementById("ticketSide").classList.toggle("show");
  document.querySelector(".mainpage").classList.toggle("grid");
  document.getElementById("total").classList.toggle("show");
}

//toggle menu
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

function displayCheckout() {
  document.getElementById("checkoutBox").classList.toggle("show");
  checkoutTotal = document.getElementById("total");
  document.getElementById("totalBox").innerHTML =
    "$" + checkoutTotal.innerHTML.substring(1);
  document.querySelector(".mainpage").classList.toggle("hide");
}

// function updateTotal() {
//   let addons = 0;
//   if (document.querySelectorAll(".sideDrop").length > 0) {
//     for (const sideDrop of document.querySelectorAll(".sideDrop")) {
//       if (
//         sideDrop.options[sideDrop.selectedIndex].value == 6 ||
//         sideDrop.options[sideDrop.selectedIndex].value == 7
//       ) {
//         addons += 2.5;
//       }
//     }
//     newTotal = total + addons;
//     totalText.innerHTML = "$" + newTotal.toFixed(2);
//   }
// }
