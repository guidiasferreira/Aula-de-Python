
peso = float (input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = round (peso / (altura **2) , 1)

if imc < 18.5:
    print("Abaixo do peso" , imc)

elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal" , imc)

elif imc >= 25 and imc <= 29.9:
    print("Acima do peso" , imc)

elif imc > 30 and imc <= 34.9:
    print("Obeso I" , imc)

elif imc > 35 and imc <= 39.9:
    print("Obeso II" , imc)

else:
    print("Obeso III" , imc)

