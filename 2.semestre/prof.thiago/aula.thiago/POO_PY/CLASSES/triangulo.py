#encapsulamento


class Triangulo:
    def __init__(self,base,altura):
        self.base= base
        self.altura= altura

    def calcular_area(self) ->float:
        area=(self.base*self.altura)/2
        return area
    
t1=Triangulo (9,15)
t2= Triangulo(4.5,6)

print('BASE DO T2: ',t2.base)

print(t2.calcular_area())

##para privar um dado uso __ e preciso criar uma def para acessar o atributo privado

   # def get_base(self:)
    #return (self.__altura)

#aqui criamos um um def que utiliza uma get para pegar uma informação privada no sistema
#como um CPF , o sistema nao mostra o caminho para um hacker, mas pode ser acessado pelo ADM e usado pelo usuario, 
# sem mostrar o caminho. 

      #  self.__base= base #agora esta privada, com o uso do underline
     #   self.__altura= altura#aqui tambem  

#preciso primeiro definir la no INIT self.__base antes de criar um def get