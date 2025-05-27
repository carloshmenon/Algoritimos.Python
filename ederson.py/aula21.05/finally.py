
try:
    a=int(input("digite uma palavra="))
except ValueError:
    print ("digite apenas numero")
    
except: 
    print("erro desconhecido")
    
finally:
    print("final do algoritmo")