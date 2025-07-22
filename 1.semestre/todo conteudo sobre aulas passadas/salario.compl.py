#calculando o salario 

vhoras= float(input("Qual valor da sua hora trabalhada? "))
qhoras= float(input("Qual a quantidade de horas trabalhadas? "))

salariobruto= qhoras*vhoras

if salariobruto <=900:
    INSS=salariobruto*0.10

IR= salariobruto*0.05

FGTS=salariobruto*0.11

Totaldedesconto= INSS+IR

salarioliquido= salariobruto-INSS-IR

print(" Salário bruto: ", "(",vhoras,")",("*"), "(",qhoras,"): R$ ",          salariobruto)

print("(-) IR (5%):             ISENTO", )

print("(-) INSS (10%):          R$",  INSS)

print("(-) FGTS (11%):          R$"  ,FGTS)

print("Total dos descontos :    R$" ,Totaldedesconto )

print("Salário liquido:         R$"  ,salarioliquido)

if salariobruto >=901 and salariobruto <=1500:
    
    print(" Salário bruto: ", "(",vhoras,")",("*"), "(",qhoras,"): R$ ",          salariobruto)

print("(-) IR (5%):             R$", IR)

print("(-) INSS (10%):          R$",  INSS)

print("(-) FGTS (11%):          R$"  ,FGTS)

print("Total dos descontos :    R$" ,Totaldedesconto )

print("Salário liquido:         R$"  ,salarioliquido)

if salariobruto >=1501 and salariobruto<=2500:
    IR= salariobruto*0.10
    
    print(" Salário bruto: ", "(",vhoras,")",("*"), "(",qhoras,"): R$ ",          salariobruto)

print("(-) IR (5%):             R$", IR)

print("(-) INSS (10%):          R$",  INSS)

print("(-) FGTS (11%):          R$"  ,FGTS)

print("Total dos descontos :    R$" ,Totaldedesconto )

print("Salário liquido:         R$"  ,salarioliquido)

if salariobruto>=2500:
    IR= salariobruto*0.20 

    print(" Salário bruto: ", "(",vhoras,")",("*"), "(",qhoras,"): R$ ",          salariobruto)

print("(-) IR (5%):             R$", IR)

print("(-) INSS (10%):          R$",  INSS)

print("(-) FGTS (11%):          R$"  ,FGTS)

print("Total dos descontos :    R$" ,Totaldedesconto )

print("Salário liquido:         R$"  ,salarioliquido)


