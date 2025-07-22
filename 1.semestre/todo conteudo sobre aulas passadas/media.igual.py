#calcule a media e faça uma media com 10

not1= float(input("digite a primeira nota: "))
not2= float(input("digite a primeira nota: "))

media=(not1+not2)/2

if media >=7 and media<=9.9:
    print("APROVADO")

if media<=6.9:
        print("REPROVADO")

elif media ==10:
        print("APROVADO COM DISTANÇÃO")
        