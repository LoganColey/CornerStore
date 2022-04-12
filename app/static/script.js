const foodbox = document.getElementById("content");
const options = document.querySelectorAll(".Btn");

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


// Review Boxes

Vue.config.devtools = true;

Vue.component('card', {
  template: `
    <div class="card-wrap"
      @mousemove="handleMouseMove"
      @mouseenter="handleMouseEnter"
      @mouseleave="handleMouseLeave"
      ref="card">
      <div class="card"
        :style="cardStyle">
        <div class="card-bg" :style="[cardBgTransform, cardBgImage]"></div>
        <div class="card-info">
          <slot name="header"></slot>
          <slot name="content"></slot>
        </div>
      </div>
    </div>`,
  mounted() {
    this.width = this.$refs.card.offsetWidth;
    this.height = this.$refs.card.offsetHeight;
  },
  props: ['dataImage'],
  data: () => ({
    width: 0,
    height: 0,
    mouseX: 0,
    mouseY: 0,
    mouseLeaveDelay: null
  }),
  computed: {
    mousePX() {
      return this.mouseX / this.width;
    },
    mousePY() {
      return this.mouseY / this.height;
    },
    cardStyle() {
      const rX = this.mousePX * 30;
      const rY = this.mousePY * -30;
      return {
        transform: `rotateY(${rX}deg) rotateX(${rY}deg)`
      };
    },
    cardBgTransform() {
      const tX = this.mousePX * -40;
      const tY = this.mousePY * -40;
      return {
        transform: `translateX(${tX}px) translateY(${tY}px)`
      }
    },
    cardBgImage() {
      return {
        backgroundImage: `url(${this.dataImage})`
      }
    }
  },
  methods: {
    handleMouseMove(e) {
      this.mouseX = e.pageX - this.$refs.card.offsetLeft - this.width/2;
      this.mouseY = e.pageY - this.$refs.card.offsetTop - this.height/2;
    },
    handleMouseEnter() {
      clearTimeout(this.mouseLeaveDelay);
    },
    handleMouseLeave() {
      this.mouseLeaveDelay = setTimeout(()=>{
        this.mouseX = 0;
        this.mouseY = 0;
      }, 1000);
    }
  }
});

const app = new Vue({
  el: '#app'
});
