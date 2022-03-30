function populatePage() {
    fetch("/static/json/big.json")
      .then((req) => req.json())
      .then((data) => {
      keys = Object.keys(data[0]);
      var table = document.createElement("table");
      var tr = table.insertRow(-1);
      for (i=0;i < keys.length;i++) {
        var th = document.createElement("th");
        th.innerHTML = keys[i];
        tr.appendChild(th);
      }
        for (const item of data) {
          console.log(item);
        }
      for (var i = 0; i < data.length; i++) {
    
        tr = table.insertRow(-1);

        for (var j = 0; j < keys.length; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = data[i][keys[j]];
        }
      }
      var divContainer = document.getElementById("Table");
      divContainer.innerHTML = "";
      divContainer.appendChild(table);  
    }
  )  
}