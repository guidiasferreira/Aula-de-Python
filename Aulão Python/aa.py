
peso = float(input("Peso:"))
altura = float(input("Altura"))

imc = round (peso / altura **2 , 2) 

if imc < 18:
    print("Leve" , imc)