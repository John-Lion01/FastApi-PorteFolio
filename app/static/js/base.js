
const form = document.querySelector("form");

form.addEventListener("submit", function(e){
    e.preventDefault();
    const formData = new FormData(this);
    const url = "/api/message";
    // console.info("soumision ..............." + url + " \n  " + formData)
    var pop = document.createElement("li");

    fetch(url, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) throw new Error('Server error 001');
        return response.json();
    }).then(data => {
        if (data.status === 'success') {
            pop.classList.add("success")
            pop.textContent = "message send successfully"
            form.reset();
        }
        
    }).catch(error => {
        pop.classList.add("error")
        pop.textContent = "Error : Réessayer plutart SVP !"
    });

    var popup = document.querySelector("div.popup ul");
    // console.log(popup + " **** ") 

    popup.appendChild(pop);
    setTimeout(() => {
        popup.removeChild(pop);
    }, 3000);
})