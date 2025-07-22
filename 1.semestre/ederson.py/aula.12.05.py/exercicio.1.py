#media de idade


soma=0
quantidade_de_alunos=int(input("digite a quantidade de alunos: \n "))  

for media in range (quantidade_de_alunos):
        idade_de_alunos=int(input("digite a idade dos alunos: \n "))  
        soma+=idade_de_alunos
media= soma/quantidade_de_alunos

if media>=25<=49:
        print("a media de idade da turma são de jovens", media, "anos")

elif media <=24:
        print("a media de idade da turma são de adoslecentes", media, "anos")

elif media >=51:
        print("a media de idade da turma são de idosos", media, "anos")



