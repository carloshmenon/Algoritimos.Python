import random
import math

# 1. Função de saudação personalizada
def saudacao(nome):
    print(f"Olá, {nome}! Seja muito bem-vindo(a)!")
saudacao("Maria")
print("\n" + "-"*50 + "\n")

# 2. Função que retorna a soma de dois números
def soma(a, b):
    return a + b
print("Soma:", soma(5, 3))
print("\n" + "-"*50 + "\n")

# 3. Função que calcula o quadrado de um número
def quadrado(num):
    return num ** 2
print("Quadrado:", quadrado(4))
print("\n" + "-"*50 + "\n")

# 4. Função que verifica se um número é par
def eh_par(num):
    return num % 2 == 0
print("É par?", eh_par(7))
print("\n" + "-"*50 + "\n")

# 5. Função que retorna o maior elemento de uma lista
def maior_elemento(lista):
    return max(lista) if lista else None
print("Maior elemento:", maior_elemento([3, 1, 4, 1, 5, 9]))
print("\n" + "-"*50 + "\n")

# 6. Função que calcula fatorial (sem recursão)
def fatorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado
print("Fatorial:", fatorial(5))
print("\n" + "-"*50 + "\n")

# 7. Função que verifica se um número é primo
def eh_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
print("É primo?", eh_primo(11))
print("\n" + "-"*50 + "\n")

# 8. Função que inverte uma string
def inverte_string(s):
    return s[::-1]
print("String invertida:", inverte_string("Python"))
print("\n" + "-"*50 + "\n")

# 9. Função que filtra nomes com mais de 5 letras
def nomes_longos(lista_nomes):
    return [nome for nome in lista_nomes if len(nome) > 5]
print("Nomes longos:", nomes_longos(["Ana", "Fernanda", "Carlos", "Jo"]))
print("\n" + "-"*50 + "\n")

# 10. Função que conta vogais em uma string
def contar_vogais(s):
    vogais = 'aeiouAEIOU'
    return sum(1 for char in s if char in vogais)
print("Vogais:", contar_vogais("Hello World"))
print("\n" + "-"*50 + "\n")

# 11. Função que retorna divisores de um número
def divisores(num):
    return [i for i in range(1, num+1) if num % i == 0]
print("Divisores:", divisores(12))
print("\n" + "-"*50 + "\n")

# 12. Função que converte Celsius para Fahrenheit
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32
print("Celsius para Fahrenheit:", celsius_para_fahrenheit(30))
print("\n" + "-"*50 + "\n")

# 13. Função que remove espaços de uma string
def remover_espacos(s):
    return s.replace(" ", "")
print("Sem espaços:", remover_espacos("Olá Mundo!"))
print("\n" + "-"*50 + "\n")

# 14. Função que calcula média de uma lista
def media_lista(lista):
    return sum(lista) / len(lista) if lista else 0
print("Média:", media_lista([1, 2, 3, 4, 5]))
print("\n" + "-"*50 + "\n")

# 15. Função que verifica palíndromo
def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]
print("É palíndromo?", eh_palindromo("radar"))
print("\n" + "-"*50 + "\n")

# 16. Função que gera n primeiros números pares
def primeiros_pares(n):
    return [2*i for i in range(1, n+1)]
print("Primeiros pares:", primeiros_pares(5))
print("\n" + "-"*50 + "\n")

# 17. Função que retorna tabuada de um número
def tabuada(num):
    return [num * i for i in range(1, 11)]
print("Tabuada:", tabuada(7))
print("\n" + "-"*50 + "\n")

# 18. Função que calcula área do retângulo
def area_retangulo(base, altura):
    return base * altura
print("Área retângulo:", area_retangulo(5, 3))
print("\n" + "-"*50 + "\n")

# 19. Função que retorna o menor de três números
def menor_de_tres(a, b, c):
    return min(a, b, c)
print("Menor de três:", menor_de_tres(5, 2, 8))
print("\n" + "-"*50 + "\n")

# 20. Função que simula lançamento de dado
def lancar_dado():
    return random.randint(1, 6)
print("Lançamento de dado:", lancar_dado())
print("\n" + "-"*50 + "\n")