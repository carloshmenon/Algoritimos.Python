// validando se tem 3 digitos
const inputs= document.querySelectorAll(".required");
// criando uma funcao para exibir o erro
const spans = document.querySelectorAll(".span-required"); // criando a constante
function nameValidate(){
    if(inputs[0].value.length<3){
        setError(0);}

    else{
        removeError(0);}
    }
    
    
    function removeError(index){
        spans[index].style.display="none";
        console.log ("tudo certo")
    }

    function setError (index){
        spans[index].style.display="block";
    }

// para multiplos elementos com uma classe, podemos utilizar document.querySlecetorALL()
// e document.getElementsByClassName(). para selecionar apenas um unico

// criando uma funcao para exibir o erro
