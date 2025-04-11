#menor produto

produto1=float(input("qual o preço do primeiro produto? "))
produto2=float(input("qual o preço do segundo produto? "))
produto3=float(input("qual o preço do terceiro produto? "))

if produto1<produto2 and produto1<produto3:
    print("o", produto1, "é o mais barato.")

if produto2<produto1 and produto2<produto3:
    print("o", produto2, "é o mais barato.")

if produto3<produto1 and produto3<produto2:
    print("o", produto3, "é o mais barato.")