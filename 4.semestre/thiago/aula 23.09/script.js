
let input_cep = document.getElementById("texto");

let bot = document.getElementById ("buscar")

bot.addEventListener('click', async function(){
    alert("clicou");
})

input_cep.addEventListener('change', async function(event){
    event.preventDefault ();

    let response = await fetch ("viacep.com.br/ws/01001000/json/")
    let data = await response.json()
});