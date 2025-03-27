#aula 24.063

#inserindo elementos ".append"

a= [81,82,83]
a .append(5)
print (a)
print("\n \n")

#ordenando os elementos da lista com ".sort" se usado .reverse é o oposto do .sort, do maior para o menor

a=[81,88,85,84]
a.sort()
print(a)
print("\n \n")

#.index, usado para localizar algo na sua lista, lembrando que os itens da lista começa com "0"

a=[1,2,3,4,5,6]
print(a.index(3))
print("\n \n")

#.insert, usado para inserir itens na sua lista
a=[88,10,66,44]
a.insert(1,100)
print(a)
print("\n \n")

#.count usado para contar quantas vezes o item desejado aparece na sua lista

a=[88,88,99,99,100,100]
print(a)
print(a.count(88))
print("\n \n")

#.pop exclui o ultimo item da minha lista, ou o item da minha escolha
a=[1,2,3,4,5,6]
a.pop()
print(a)
print("\n")

a.pop(2)
print(a)
print("\n \n")

# .extend adiciona itens no final da sua lista 

a=[1,2,3]
a.extend([4,5])
print (a)