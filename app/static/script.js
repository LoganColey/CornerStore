const foodbox = document.getElementById("content");
const ticketDisplay = document.getElementById("ticketDisplay");
const options = document.querySelectorAll(".Btn");
const itemsList = [];

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
                </article>
              `
    );
  }
}

function populateInitialContent() {
  fetch("/static/food.json")
    .then((req) => req.json())
    .then((data) => {
      populateContent(data);
    });
}

function populateTickets() {
  if (itemsList.length > 0) {
    ticketDisplay.innerHTML = "";
    for (const item of itemsList) {
      ticketDisplay.insertAdjacentHTML(
        "beforeend",
        `
                  <article class="itemBox">
                      <h2 class="itemName">${item.name}</h2>
                      <img src=/static/images/${item.image}></img>
                      <h2 class="itemPrice">$ ${item.cost}</h2>
                  </article>
                `
      );
    }
  }
}d
