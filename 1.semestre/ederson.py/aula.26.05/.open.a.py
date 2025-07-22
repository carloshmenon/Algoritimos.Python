#adicionando conteudo ao arquivo, abrimos arquivos com "a" de apeend, depois colocamos para leitura "r". podemos tambem colocar um input e uma variavel que o usuario ira digitar 
# e guardar a informação do usuario
#encoding utf-8. aceita caracteres especiais como ç no codigo
#usando "a ele cria arquivos automaticos, usado para log, como data e hora"

f=open("ederson.py/aula.26.05/file.txt","a", encoding="utf-8")
f.write(f"\n adionando conteúdo! \n")
f=open("ederson.py/aula.26.05/file.txt","r")
print(f.read())
f.close()