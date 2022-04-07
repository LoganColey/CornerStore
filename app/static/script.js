const foodbox = document.getElementById("content");
const ticketDisplay = document.getElementById("ticketDisplay");
const options = document.querySelectorAll(".Btn");
const itemsList = [];
const ticketList = [];

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
          populateContent(leList);
        });
    }
  });
});

function populateContent(items) {
  foodbox.innerHTML = "";
  for (const item of items) {
    foodbox.insertAdjacentHTML(
      "beforeend",
      `
                <article class="itemBox">
                    <h2 class="itemName">${item.name}</h2>
                    <img src=/static/images/${item.image}></img>
                    <p class="itemDesc">${item.description}</p>
                    <h2 class="itemPrice">$ ${item.cost}</h2>
                    <button style="width: 5em; height: 5em"class="addListBtn">Add To Ticket!!</button>
                </article>
              `
    );
  }
  buttons();
}

function populateInitialContent() {
  fetch("/static/food.json")
    .then((req) => req.json())
    .then((data) => {
      populateContent(data);
      for (const item of data) {
        itemsList.push(item);
      }
    });
  buttons();
}

function buttons() {
  var AddItemBtns = document.getElementsByClassName("addListBtn");
  for (let i = 0; i < AddItemBtns.length; i++) {
    var button = AddItemBtns[i];
    button.addEventListener("click", AddItem);
  }
}

function loadTicket() {
  if (ticketList.length > 0) {
    ticketDisplay.innerHTML = "";
  }
}

function AddItem(event) {
  var button = event.target;
  var item_card = button.parentElement;
  ticketList.push(
    itemsList.filter(
      (item) =>
        item.name == item_card.getElementsByClassName("itemName")[0].innerText
    )
  );
  console.log(ticketList);
  for (const item of ticketList) {
    var wholeItem = document.createElement("div");
    wholeItem.classList.add("whole");
    wholeItem.insertAdjacentHTML(
      "beforeend",
      `<article>
        <div>
          <div>
            <p class="item_name">${item[0].name}</p>
          </div>
          <div>
            <p class="itemPrice">$${item[0].cost}</p>
          </div>
          <button class="removeItem">Remove</button>
        </div>
      </article>`
    );
  }
  ticketDisplay.append(wholeItem);
  let buttons = ticketDisplay.getElementsByClassName("removeItem");
  for (let i = 0; i < buttons.length; i++) {
    var variable = buttons[i];
    variable.addEventListener("click", removeItem);
  }
}

function removeItem(event) {
  var buttonClicked = event.target;
  buttonClicked.parentElement.parentElement.remove();
}
