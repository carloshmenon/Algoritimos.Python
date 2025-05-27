#usando o "r read" com o "b de binario" ou "t de texto"

f=open("ederson.py/aula.26.05/file.txt","rb", encoding="utf-8")
f.write(f"\n adionando conteúdo 2! \n")
f=open("ederson.py/aula.26.05/file.txt","r")
print(f.read())
f.close()