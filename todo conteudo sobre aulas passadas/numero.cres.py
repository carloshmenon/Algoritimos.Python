#ordem crescente

num1= int(input("digite um numero: "))
num2= int(input("digite um numero: "))
num3= int(input("digite um numero: "))

if num3>num1 and num1>num2:
    print(num3, num1, num2)

#num3= 3 
#num1= 2
#num2=1

elif num3>num2 and num2>num1:
    print(num3, num2, num1)

#num3= 3 
#num2= 2
#num1=1

elif num2>num1 and num1>num2:
    print(num2, num1, num3)

#num2= 3 
#num1= 2
#num3=1

elif num2>num3 and num3>num1:
    print(num2, num3, num1)

#num2= 3 
#num3= 2
#num1=1

elif num1>num2 and num2>num3:
    print(num1, num2, num3)  

#num1= 3 
#num2= 2
#num3=1  

elif num1>num3 and num3>num2:
    print(num1, num3, num2)

#num1= 3 
#num3= 2
#num2=1
   
   