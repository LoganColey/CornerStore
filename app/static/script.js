const foodbox = document.getElementById("content");
const ticketDisplay = document.getElementById("ticketDisplay");
const options = document.querySelectorAll(".Btn");
let total = 0;
const totalText = document.getElementById("total");
var dt = new Date();
const sidesNames = [];

fetch("/static/food.json")
  .then((req) => req.json())
  .then((data) => {
    console.log(data);
    for (const item of data) {
      if (item.type == "side") {
        sidesNames.push(item.name);
      }
    }
  });

//makes menu dropdown buttons work
options.forEach((m) => {
  m.addEventListener("click", (e) => {
    if (e.target.innerHTML === "Burgers and More") {
      foodbox.innerHTML = "";
      fetchingAndPopulating("small", "Burgers and More");
    } else if (e.target.innerHTML === "Sides") {
      foodbox.innerHTML = "";
      fetchingAndPopulating("side", "Sides");
    } else if (e.target.innerHTML === "Plates") {
      foodbox.innerHTML = "";
      fetchingAndPopulating("big", "Plates");
    } else if (e.target.innerHTML === "Salads") {
      foodbox.innerHTML = "";
      fetchingAndPopulating("salad", "Salads");
    } else if (e.target.innerHTML === "Starters") {
      foodbox.innerHTML = "";
      fetchingAndPopulating("starter", "Starters");
    } else if (e.target.innerHTML === "Seafood") {
      foodbox.innerHTML = "";
      fetchingAndPopulating("seafood", "Seafood");
    }
  });
});

//the initialize function of the page
function populateInitialContent() {
  fetchingAndPopulating("starter", "Starters");
  fetchingAndPopulating("small", "Burgers and More");
  fetchingAndPopulating("big", "Plates");
  fetchingAndPopulating("side", "Sides");
  fetchingAndPopulating("salad", "Salads");
  if (dt.getDay() == 5 || dt.getDay() == 6) {
    fetchingAndPopulating("seafood", "Seafood");
  }
}

//fetch from json and put it on screen and make the buttons work
function fetchingAndPopulating(foodType, foodName) {
  fetch("/static/food.json")
    .then((req) => req.json())
    .then((data) => {
      console.log(data);
      var platesHeader = document.createElement("header");
      platesHeader.innerHTML = foodName;
      platesHeader.classList.add("full-width");
      foodbox.appendChild(platesHeader);
      var leList = [];
      for (const item of data) {
        if (item.type == foodType) {
          leList.push(item);
        }
      }
      var itemsbox = document.createElement("div");
      itemsbox.classList.add("items");
      foodbox.appendChild(itemsbox);
      for (const item of leList) {
        var roundedCost = item.cost.toFixed(2);
        itemsbox.insertAdjacentHTML(
          "beforeend",
          `
                    <article id="itemBox" class="${item.type}">
                        <h2 class="itemName">${item.name}</h2>
                        <img src=/static/images/bigchungus.png></img>
                        <p class="itemDesc">${item.description}</p>
                        <h2 class="itemPrice">$ ${roundedCost}</h2>
                        <button style="width: 5em; height: 5em"class="addListBtn">Add To Ticket!!</button>
                    </article>
                  `
        );
      }
      var AddItemBtns = document.getElementsByClassName("addListBtn");
      for (let i = 0; i < AddItemBtns.length; i++) {
        var button = AddItemBtns[i];
        button.addEventListener("click", AddItem);
      }
    });
}

//adding an item to the ticket
function AddItem(event) {
  document.querySelector(".checkoutbtn").classList.add("show");
  var button = event.target;
  var item_card = button.parentElement;
  var item_name = item_card.getElementsByClassName("itemName")[0].innerText;
  var item_price_string =
    item_card.getElementsByClassName("itemPrice")[0].innerText;
  var item_price = item_price_string.substring(1);
  var wholeItem = document.createElement("div");
  wholeItem.classList.add("whole");
  wholeItem.insertAdjacentHTML(
    "beforeend",
    `
      <div>
        <div>
          <p class="item-name">${item_name}</p>
        </div>
        <div>
          <p class="item-price">$${item_price}</p>
        </div>
        <button class="removeItem">Remove</button>
      </div>`
  );
  // small food side dropdown creation
  if (item_card.className == "small") {
    let sideDropdown = document.createElement("select");
    wholeItem.append(sideDropdown);
    sideDropdown.classList.add("sideDrop");
    let sidePlaceholder = document.createElement("option");
    sidePlaceholder.value = 0;
    sidePlaceholder.innerHTML = "Choose a side";
    sideDropdown.appendChild(sidePlaceholder);
    let i = 1;
    for (const side of sidesNames) {
      let newSide = document.createElement("option");
      newSide.innerHTML = side;
      sideDropdown.append(newSide);
      newSide.value = i;
      i += 1;
    }
    sideDropdown.addEventListener("change", updateTotal);

    //big food side dropdowns
  } else if (item_card.className == "big") {
    let sidesDiv = document.createElement("div");
    wholeItem.append(sidesDiv);
    let sideDropdown = document.createElement("select");
    sideDropdown.classList.add("sideDrop");
    sidesDiv.append(sideDropdown);
    let sidePlaceholder = document.createElement("option");
    sidePlaceholder.value = 0;
    sidePlaceholder.innerHTML = "Choose a side";
    sideDropdown.appendChild(sidePlaceholder);
    i = 1;
    for (const side of sidesNames) {
      let newSide = document.createElement("option");
      newSide.innerHTML = side;
      sideDropdown.append(newSide);
      newSide.value = i;
      i += 1;
    }
    sideDropdown.addEventListener("change", updateTotal);
    let sideDropdown2 = document.createElement("select");
    sidesDiv.append(sideDropdown2);
    let sidePlaceholder2 = document.createElement("option");
    sideDropdown2.classList.add("sideDrop");
    sidePlaceholder2.value = 0;
    sidePlaceholder2.innerHTML = "Choose a side";
    i = 1;
    sideDropdown2.appendChild(sidePlaceholder2);
    for (const side of sidesNames) {
      let newSide = document.createElement("option");
      newSide.innerHTML = side;
      sideDropdown2.append(newSide);
      newSide.value = i;
      i += 1;
    }
    sideDropdown2.addEventListener("change", updateTotal);
  }

  ticketDisplay.append(wholeItem);
  let buttons = ticketDisplay.getElementsByClassName("removeItem");
  let sideSelectors = ticketDisplay.getElementsByClassName("sideSelector");
  for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", removeItem);
  }
  for (let i = 0; i < sideSelectors.length; i++) {
    var variable = sideSelectors[i];
    variable.addEventListener("click", sideSelection);
  }
  total += Number(item_price);
  totalText.innerHTML = "";
  totalText.innerHTML = "$" + total.toFixed(2);
}

function removeItem(event) {
  var button = event.target;
  var item_card = button.parentElement;
  var item_price = item_card
    .getElementsByClassName("item-price")[0]
    .innerText.substring(1);
  total -= Number(item_price);
  totalText.innerHTML = "";
  if (total <= 0) {
    document.querySelector(".checkoutbtn").classList.remove("show");
    totalText.innerHTML = "$0.00";
  } else {
    totalText.innerHTML = "$" + total.toFixed(2);
  }
  button.parentElement.parentElement.remove();
}

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
  if (dt.getDay() == 5 || dt.getDay() == 6) {
    document.getElementById("seafood").classList.remove("hide");
    document.getElementById("seafood").classList.add("show");
  } else {
    document.getElementById("seafood").classList.remove("show");
    document.getElementById("seafood").classList.add("hide");
  }
}

function displayCheckout() {
  document.getElementById("checkoutBox").classList.toggle("show");
  checkoutTotal = document.getElementById("total");
  document.getElementById("totalBox").innerHTML =
    "$" + checkoutTotal.innerHTML.substring(1);
  document.querySelector(".mainpage").classList.toggle("hide");
}

function updateTotal() {
  let addons = 0;
  if (document.querySelectorAll(".sideDrop").length > 0) {
    for (const sideDrop of document.querySelectorAll(".sideDrop")) {
      if (
        sideDrop.options[sideDrop.selectedIndex].value == 6 ||
        sideDrop.options[sideDrop.selectedIndex].value == 7
      ) {
        addons += 2.5;
      }
    }
    newTotal = total + addons;
    totalText.innerHTML = "$" + newTotal.toFixed(2);
  }
}
