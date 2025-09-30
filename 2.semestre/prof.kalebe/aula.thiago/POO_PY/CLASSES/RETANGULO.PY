
class Retangulo:
    def __init__(self,base,altura):
        self.base =base
        self.altura= altura

    def calcula_area (self):
        return self.altura* self.base #o self atribui oque quero multiplicar, usando self, pego direto a função
    
r1= Retangulo(12,24)#aqui inseri o valor 
print(r1.base)#aqui mostro o dado qe recebi
print(r1.altura)#aqui tambem
r2= Retangulo(8,12)#aqui inseri o valor 

x=r1.calcula_area()#aqui defini que o x calcula o retangulo r1

y= r2.calcula_area()#aqui defini que o x calcula o retangulo r2

print("AREA: ", x)#aqui mostro o resultado
print("AREA: ", x)#aqui mostro o resultado


