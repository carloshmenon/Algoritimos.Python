

let form = document.getElementById("formulario")

console.log(form)




let bot_cadastrar = document.getElementById("cadastrar")

bot_cadastrar.addEventListener('click', function(event){

    event.preventDefault();

    let nome=document.getElementById("nome").value;
    let cpf=document.getElementById("cpf").value;
    let cidade=document.getElementById("cidade").value;

    if(cidade.lenght <=2){
        alert("favor preencher a cidade!")
    }

    alert('clicouuu!!!!');
    console.log(form);
    console.log(nome);
    console.log(cpf);
    console.log(cidade);

});