#.open lendo arquivos com o "r" read, colocar todo endereço da pasta do arquivo, por exemplo "ederson.py/aula.26.05/file.txt","r"


f=open("ederson.py/aula.26.05/file.txt","r")
print(f.read())
f.close()