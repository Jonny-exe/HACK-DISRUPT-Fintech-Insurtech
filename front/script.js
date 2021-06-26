const URL = "http://localhost:5000/file"
console.log("HELLO")
const send = async () => {
   const {data} = await axios.post(URL, `text=${inputText.value}`)
   console.log(data)


   let trs = ""
   for (let i = 0; i < data.length; i++) {
      a = data[i]
      let tr = `
         <tr>
         <td>${a["product"]}</td>
         <td>${a["co2"]}</td>
      </tr>
      `
      trs = trs + tr
   }

   let body = `
<tbody>
   ${trs}
</tbody>
`
   table.innerHTML = `
<thead>
   <tr>
      <th scope="col">Producto</th>
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
   console.log(labels)
   const keys = Object.keys(labels)

   for (let key in keys) {
      key = keys[key]
      l.push(key)
      d.push(labels[key])
      console.log(key, labels[key])
   }
   console.log(l, d)
   const da = {
      labels: l,
        datasets: [{
               label: 'Categories',
               data: d,
               backgroundColor: [
                 'rgb(255, 99, 132)',
                 'rgb(54, 162, 235)',
                 'rgb(255, 205, 86)'
               ],
               hoverOffset: 4
             }]
   };

   const config = {
      type: 'doughnut',
      data: da,
   };

   var myChart = new Chart(
      document.getElementById('myChart'),
      config
   );

}
const inputText = document.getElementById("input-text")
const submitButton = document.getElementById("submit-button")
const table = document.getElementById("table")

submitButton.addEventListener("click", send)

