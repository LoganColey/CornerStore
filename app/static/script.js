const foodbox = document.getElementById("content");
const options = document.querySelectorAll(".Btn");

options.forEach((m) => {
  m.addEventListener("click", (e) => {
    console.log(e.target.innerHTML);
    fetch("/static/json/" + e.target.name + ".json")
      .then((req) => req.json())
      .then((data) => {
        populateContent(data);
      });
  });
});

function populateContent(items) {
  console.log(foodbox.innerHTML);
  foodbox.innerHTML = "";
  for (const item of items) {
    foodbox.insertAdjacentHTML(
      "beforeend",
      `
              <article class = "foodItem" style="background-color: lightgray">
                <div style="margin-left: 2em; padding-top:3em">
                    <h2 class="itemName">${item.name}</h2>
                    <img src=/static/images/${item.image}></img>
                    <p class="itemDesc">${item.description}</p>
                    <h2 class="itemPrice">${item.cost}</h2>
                </div>
              </article>
              `
    );
  }
}

