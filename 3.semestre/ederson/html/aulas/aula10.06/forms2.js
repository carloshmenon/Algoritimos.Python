const inputs = document.querySelectorAll(".required");
const spans = document.querySelectorAll(".span-required");

function passwordValidate1(){
    if (inputs[0].value.length>=8){
        removeError(0);
    }

    else{
        setError(0);
    }
}

function passwordValidate2(){
    if (inputs[1].value.length>=8 && inputs[0].value== inputs[1].value){
        removeError(1);
    }

    else{
        setError(1);
    }
}

function setError(index){
    spans[index].style.display="block";
}

function removeError(index){
    spans[index].style.display="none";
}

// a partir de agora, se os caracteres do primeiro forms forem menor do que 8 a funcao setError ()na posicao 0
// sera exibida, senao a funcao removeError () nao posicao 0 será executada.