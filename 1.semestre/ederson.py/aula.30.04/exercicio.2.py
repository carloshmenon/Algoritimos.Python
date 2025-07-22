#urna eletronica, print maior candidado, caso o usuario de enter

candi1=0
candi2=0
candi3=0
candi4=0
nulo=0
votobranco=0
voto=[candi1,candi2,candi3,candi4]
maior=(max(voto))
while True:

    voto= int (input("digite o numero do candidato, 1-4, 5 sendo nulo e 6 sendo voto em branco : \n"))


    if voto ==0:
        print("votação encerrada \n")
        break                            
    elif voto == 1: 
        candi1 +=1

    elif voto == 2:
        candi2 +=1

    elif voto == 3:
        candi3 +=1

    elif voto == 4:
        candi4 +=1

    elif voto == 5:
        nulo +=1

    elif votobranco ==6:
       votobranco +=1

print("resultado da votação\n")


print(maior)

#print(max(voto))
#print("votos candidato 2", {candi2},"\n")
#print("votos candidato 3", {candi3},"\n")
#print("votos candidato 4", {candi4},"\n")
#print("votos nulos", {nulo},"\n")
#print("votos em branco", {votobranco},"\n")








   
          
