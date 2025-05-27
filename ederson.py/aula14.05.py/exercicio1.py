#traduzindo a palavra com dicionario



tradutor =str(input("escreva uma palavra: \n"))


tradutor_portugues_ingles={"apple":"maçã","orange":"laranja","banana":"banana","grape":"uva","pineapple":"abacaxi",
"strawberry":"morango","watermelon":"melancia","lemon":"limão","lime":"lima","peach":"pêssego",
"plum":"ameixa","cherry":"cereja","mango":"manga","papaya":"mamão","kiwi":"kiwi",
"blueberry":"mirtilo","raspberry":"framboesa","blackberry":"amora","coconut":"coco","melon":"melão",
"carrot":"cenoura","onion":"cebola","garlic":"alho","potato":"batata","tomato":"tomate",
"lettuce":"alface","spinach":"espinafre","cucumber":"pepino","broccoli":"brócolis","cauliflower":"couve-flor",
"corn":"milho","pea":"ervilha","bean":"feijão","pumpkin":"abóbora","zucchini":"abobrinha",
"eggplant":"berinjela","pepper":"pimentão","celery":"aipo","radish":"rabanete","beet":"beterraba",
"cow":"vaca","pig":"porco","sheep":"ovelha","goat":"cabra","chicken":"galinha",
"duck":"pato","horse":"cavalo","donkey":"burro","dog":"cachorro","cat":"gato",
"bird":"pássaro","fish":"peixe","shark":"tubarão","whale":"baleia","dolphin":"golfinho",
"tiger":"tigre","lion":"leão","elephant":"elefante","monkey":"macaco","giraffe":"girafa",
"zebra":"zebra","bear":"urso","wolf":"lobo","fox":"raposa","deer":"veado",
"ant":"formiga","bee":"abelha","butterfly":"borboleta","spider":"aranha","fly":"mosca",
"mosquito":"mosquito","snake":"cobra","frog":"sapo","lizard":"lagarto","turtle":"tartaruga",
"sun":"sol","moon":"lua","star":"estrela","sky":"céu","cloud":"nuvem",
"rain":"chuva","snow":"neve","wind":"vento","storm":"tempestade","lightning":"raio",
"fire":"fogo","water":"água","earth":"terra","air":"ar","rock":"rocha",
"sand":"areia","mountain":"montanha","river":"rio","lake":"lago","ocean":"oceano",
"tree":"árvore","flower":"flor","leaf":"folha","grass":"grama","root":"raiz",
"branch":"galho","trunk":"tronco","forest":"floresta","desert":"deserto","valley":"vale",
"house":"casa","building":"prédio","room":"quarto","kitchen":"cozinha","bathroom":"banheiro",
"bed":"cama","chair":"cadeira","table":"mesa","sofa":"sofá","window":"janela",
"door":"porta","floor":"chão","ceiling":"teto","wall":"parede","roof":"telhado",
"school":"escola","student":"aluno","teacher":"professor","book":"livro","pen":"caneta",
"pencil":"lápis","paper":"papel","desk":"escrivaninha","board":"quadro","lesson":"lição",
"computer":"computador","keyboard":"teclado","mouse":"mouse","screen":"tela","printer":"impressora",
"internet":"internet","email":"email","file":"arquivo","folder":"pasta","document":"documento",
"phone":"telefone","cellphone":"celular","charger":"carregador","battery":"bateria","camera":"câmera",
"music":"música","song":"canção","singer":"cantor","band":"banda","guitar":"violão",
"piano":"piano","drum":"bateria","violin":"violino","flute":"flauta","microphone":"microfone",
"movie":"filme","actor":"ator","actress":"atriz","cinema":"cinema","ticket":"ingresso",
"car":"carro","bus":"ônibus","train":"trem","airplane":"avião","boat":"barco",
"bicycle":"bicicleta","motorcycle":"moto","road":"estrada","street":"rua","traffic":"trânsito",
"bank":"banco","money":"dinheiro","coin":"moeda","credit":"crédito","debit":"débito",
"job":"trabalho","salary":"salário","boss":"chefe","worker":"trabalhador","office":"escritório",
"market":"mercado","store":"loja","shop":"loja","price":"preço","discount":"desconto",
"food":"comida","drink":"bebida","bread":"pão","meat":"carne","cheese":"queijo",
"milk":"leite","egg":"ovo","rice":"arroz","beans":"feijão","soup":"sopa",
"sugar":"açúcar","salt":"sal","oil":"óleo","butter":"manteiga","cake":"bolo"
}

if tradutor==tradutor_portugues_ingles:
    print(tradutor_portugues_ingles[tradutor])

else:
    print('palavra nao encontrada')