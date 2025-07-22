#deleta arquivos com comando "w", nesse caso foi sobre escrito com a frase adiconando conteudo 2, a str que estava no txt foi aparaga e colocada essa frase

f=open("ederson.py/aula.26.05/file.txt","w", encoding="utf-8")
f.write(f"\n adionando conteúdo 2! \n")
f=open("ederson.py/aula.26.05/file.txt","r")
print(f.read())
f.close()