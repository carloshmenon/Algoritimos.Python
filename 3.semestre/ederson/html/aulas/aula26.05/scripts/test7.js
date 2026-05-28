

let a =10;
let b = 5;
let c = 20;

let test1= (a>b) && (c>b); // funcao usando and

let test2=(a<=b)||(b<=c); // usando funcao or

let test3 = !x;
let test4 = !x &&x;

console.log(test1);
console.log(test2);
console.log(test3);
console.log(test4);

if ((a>b)&&(c>b)){
    console.log("entrou no if");
}