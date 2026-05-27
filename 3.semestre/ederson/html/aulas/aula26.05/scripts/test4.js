document.write("<h1> my page </h1>")

let lista = [10,20,30,40,50,60]
console.log(lista)

for(var x =0; x<lista.length; x++){
    console.log(lista[x]);
}

let i=0;
while(i<lista.length){
    document.write("<br>");
    document.write(lista[i]);
    i++;
}