const foodbox = document.getElementById("content");
const ticketDisplay = document.getElementById("ticketDisplay");
const options = document.querySelectorAll(".Btn");
let total = 0;
const totalText = document.getElementById("total");
var dt = new Date();
let neededSides = [];
let sides = [];
const sidesNames = [];

//makes menu dropdown buttons work
options.forEach((m) => {
  m.addEventListener("click", (e) => {
    if (e.target.innerHTML === "Small") {
      let leList = [];
      fetch("/static/food.json")
        .then((req) => req.json())
        .then((data) => {
          for (const item of data) {
            if (item.type == "small") {
              leList.push(item);
            }
          }
          foodbox.innerHTML = "";
          populateContent(leList);
        });
    } else if (e.target.innerHTML === "Sides") {
      let leList = [];
      fetch("/static/food.json")
        .then((req) => req.json())
        .then((data) => {
          for (const item of data) {
            if (item.type == "side") {
              leList.push(item);
            }
          }
          foodbox.innerHTML = "";
          populateContent(leList);
        });
    } else if (e.target.innerHTML === "Big") {
      let leList = [];
      fetch("/static/food.json")
        .then((req) => req.json())
        .then((data) => {
          for (const item of data) {
            if (item.type == "big") {
              leList.push(item);
            }
          }
          foodbox.innerHTML = "";
          populateContent(leList);
        });
    } else if (e.target.innerHTML === "Salads") {
      let leList = [];
      fetch("/static/food.json")
        .then((req) => req.json())
        .then((data) => {
          for (const item of data) {
            if (item.type == "salad") {
              leList.push(item);
            }
          }
          foodbox.innerHTML = "";
          populateContent(leList);
        });
    } else if (e.target.innerHTML === "Starters") {
      let leList = [];
      fetch("/static/food.json")
        .then((req) => req.json())
        .then((data) => {
          for (const item of data) {
            if (item.type == "starter") {
              leList.push(item);
            }
          }
          foodbox.innerHTML = "";
          populateContent(leList);
        });
    }
  });
});

//creates html for items of certain type
function populateContent(items) {
  var itemsbox = document.createElement("div");
  itemsbox.classList.add("items");
  foodbox.appendChild(itemsbox);
  for (const item of items) {
    var roundedCost = item.cost.toFixed(2);
    itemsbox.insertAdjacentHTML(
      "beforeend",
      `
                <article id="itemBox" class="${item.type}">
                    <h2 class="itemName">${item.name}</h2>
                    <img src=/static/images/${item.image}></img>
                    <p class="itemDesc">${item.description}</p>
                    <h2 class="itemPrice">$ ${roundedCost}</h2>
                    <button style="width: 5em; height: 5em"class="addListBtn">Add To Ticket!!</button>
                </article>
              `
    );
  }
  buttons();
}

//the initialize function of the page
function populateInitialContent() {
  fetch("/static/food.json")
    .then((req) => req.json())
    .then((data) => {
      var startersHeader = document.createElement("header");
      startersHeader.innerHTML = "Starters";
      startersHeader.classList.add("full-width");
      foodbox.appendChild(startersHeader);
      var leList = [];
      for (const item of data) {
        if (item.type == "starter") {
          leList.push(item);
        }
      }
      populateContent(leList);
      var burgersHeader = document.createElement("header");
      burgersHeader.innerHTML = "Burgers and More";
      burgersHeader.classList.add("full-width");
      foodbox.appendChild(burgersHeader);
      var leList = [];
      for (const item of data) {
        if (item.type == "small") {
          leList.push(item);
        }
      }
      populateContent(leList);
      var platesHeader = document.createElement("header");
      platesHeader.innerHTML = "Plates";
      platesHeader.classList.add("full-width");
      foodbox.appendChild(platesHeader);
      var leList = [];
      for (const item of data) {
        if (item.type == "big") {
          leList.push(item);
        }
      }
      populateContent(leList);
      var sidesHeader = document.createElement("header");
      sidesHeader.innerHTML = "Sides";
      sidesHeader.classList.add("full-width");
      foodbox.appendChild(sidesHeader);
      var leList = [];
      for (const item of data) {
        if (item.type == "side") {
          sidesNames.push(item.name);
          leList.push(item);
        }
      }
      populateContent(leList);
      var saladsHeader = document.createElement("header");
      saladsHeader.innerHTML = "Salads";
      saladsHeader.classList.add("full-width");
      foodbox.appendChild(saladsHeader);
      var leList = [];
      for (const item of data) {
        if (item.type == "salad") {
          leList.push(item);
        }
      }
      populateContent(leList);
      if (dt.getDay() == 5 || dt.getDay() == 6) {
        var seafoodHeader = document.createElement("header");
        seafoodHeader.innerHTML = "Seafood";
        seafoodHeader.classList.add("full-width");
        foodbox.appendChild(seafoodHeader);
        var leList = [];
        for (const item of data) {
          if (item.type == "seafood") {
            leList.push(item);
          }
        }
        populateContent(leList);
      }
    });
  buttons();
}

//makes the add buttons work
function buttons() {
  var AddItemBtns = document.getElementsByClassName("addListBtn");
  for (let i = 0; i < AddItemBtns.length; i++) {
    var button = AddItemBtns[i];
    button.addEventListener("click", AddItem);
  }
}

//adding an item to the ticket
function AddItem(event) {
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
    `<article>
      <div>
        <div>
          <p class="item-name">${item_name}</p>
        </div>
        <div>
          <p class="item-price">$${item_price}</p>
        </div>
        <button class="removeItem">Remove</button>
      </div>
    </article>`
  );
  // small food side dropdown creation
  if (item_card.className == "small") {
    var side1 = document.createElement("div");
    side1.innerHTML = "Choose a side";
    side1.style.border = "1px solid black";
    var sideDropdown = document.createElement("div");
    for (const name of sidesNames) {
      var sideDiv = document.createElement("div");
      sideDiv.innerHTML = name;
      sideDropdown.append(sideDiv);
    }
    sideDropdown.setAttribute("id", "sideDropdown");
    side1.onclick = showToggle();
    sideDropdown.style.display = "none";
    wholeItem.append(side1);
    wholeItem.append(sideDropdown);
  }
  ticketDisplay.append(wholeItem);
  let buttons = ticketDisplay.getElementsByClassName("removeItem");
  for (let i = 0; i < buttons.length; i++) {
    var variable = buttons[i];
    variable.addEventListener("click", removeItem);
  }
  total += Number(item_price);
  totalText.innerHTML = "";
  totalText.innerHTML = "$" + total.toFixed(2);
}

function removeItem(event) {
  var button = event.target;
  var item_card = button.parentElement;
  var item_price_string =
    item_card.getElementsByClassName("item-price")[0].innerText;
  var item_price = item_price_string.substring(1);
  total -= Number(item_price);
  totalText.innerHTML = "";
  if (total <= 0) {
    totalText.innerHTML = "$0.00";
  } else {
    totalText.innerHTML = "$" + total.toFixed(2);
  }
  button.parentElement.parentElement.remove();
}

function showToggle() {
  document.getElementById("sideDropdown").classList.toggle("show");
}
