const URL = "http://localhost:5000/file"
console.log("HELLO")
const send = () => {
   axios.post(URL, `text=${inputText.value}`)
}
// inputElement = document.getElementById("input-field")
inputText = document.getElementById("input-text")
submitButton = document.getElementById("submit-button")

submitButton.addEventListener("click", send)

// inputElement.onchange = async function (event) {
//    let fileList = event.target.files
//    let file
//    if (fileList.length > 1) {
//       throw "Two many files"
//    } else {
//       file = fileList[0]
//    }
//    console.log(typeof(file))
//    let fd = new FormData()
//    fd.append('file', file)

//    try {
//       // response = await fetch(URL, {
//       //    method: "POST",
//       //    headers: {
//       //       'Content-Type': 'multipart/form-data'
//       //    },
//       //    body: fd
//       // })
//       response = axios.post(URL, "asdf \n asdf")
//       console.log(response)
//    }
//    catch {
//       console.log("Conexion error")
//    }
// }