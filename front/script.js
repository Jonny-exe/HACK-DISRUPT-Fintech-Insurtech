const URL = "http://localhost:5000/file"
const chart = document.getElementById('myChart')
chart.style.display = "none"
const send = async () => {
   const {data} = await axios.post(URL, `text=${inputText.value}`)
   console.log(data)

   let trs = ""
   let sum = 0
   for (let i = 0; i < data.length; i++) {
      a = data[i]
      sum += a["co2"]
      let tr = `
         <tr>
         <td>${a["product"]}</td>
         <td>${a["category"]}</td>
         <td>${a["co2"]}</td>
      </tr>
      `
      trs = trs + tr
   }
   let tr = `
      <tr>
      <td>Suma total</td>
      <td>Categorias mixtas</td>
      <td>${Math.round(sum)}</td>
   </tr>
   `
   trs = trs + tr

   let body = `
<tbody>
   ${trs}
</tbody>
`
   table.innerHTML = `
<thead>
   <tr>
      <th scope="col">Producto</th>
      <th scope="col">Categoria</th>
      <th scope="col">CO2 (KG)</th>
   </tr>
   ${body}
</thead>
   `
   let labels = {}
   for (let i = 0; i < data.length; i++) {
      a = data[i]
      if (labels[a["category"]] == null || labels[a["category"]] == undefined) {
         labels[a["category"]] = a["co2"]
      } else {
         labels[a["category"]] += a["co2"]
      }
   }

   let l = []
   let d = []
   const keys = Object.keys(labels)

   for (let key in keys) {
      key = keys[key]
      l.push(key)
      d.push(labels[key])
   }

   chart.style.display = "inherit"
   myChart.data.datasets[0].data = d
   myChart.data.labels = l
   console.log(myChart.data)
   myChart.update()

}
const inputText = document.getElementById("input-text")
const submitButton = document.getElementById("submit-button")
const table = document.getElementById("table")

submitButton.addEventListener("click", send)


const data = {
   labels: ["hello"],
   datasets: [{
      label: 'Categories',
      data: [1],
      backgroundColor: [
         //'rgb(255, 99, 132)',
         //'rgb(54, 162, 235)',
         //'rgb(255, 205, 86)'
         "blue",
         "red",
         "green"
      ],
      hoverOffset: 4
   }]
};

const config = {
     type: 'doughnut',
     data: data,
};

var myChart = new Chart(
   chart,
   config
);
