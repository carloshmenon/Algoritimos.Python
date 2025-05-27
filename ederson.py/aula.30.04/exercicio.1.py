#urna eletronica 
enceravotação=0
candi1=0
candi2=0
candi3=0
candi4=0
nulo=0
votobranco=0


while True:
    codigo= int(input("digite o numero do candidato, 1-4, 5 sendo nulo e 6 sendo voto em branco : \n"))


    if codigo==0:
        print("votação encerrada")
        break                            
    elif codigo == 1: 
        candi1 +=1

    elif codigo == 2:
        candi2 +=1

    elif codigo ==3:
        candi3 +=1

    elif codigo==4:
        candi4 +=1

    elif codigo==5:
        nulo +=1

    elif votobranco==6:
        votobranco +=1

print("resultado da votação\n")
print("votos candidato 1", {candi1},"\n")
print("votos candidato 2", {candi2},"\n")
print("votos candidato 3", {candi3},"\n")
print("votos candidato 4", {candi4},"\n")
print("votos nulos", {nulo},"\n")
print("votos em branco", {votobranco},"\n")








   
          
