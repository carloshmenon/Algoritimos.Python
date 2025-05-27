# "x" cria um arquivo que nao vai sobreescrever um arquivo acidentalmente 

f=open("ederson.py/aula.26.05/file.txt","x", encoding="utf-8")
f.write(f"\n adionando conteúdo 2! \n")
f=open("ederson.py/aula.26.05/file.txt","r")
print(f.read())
f.close()