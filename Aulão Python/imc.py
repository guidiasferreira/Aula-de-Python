
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = round (peso / (altura **  2) , 1) 

if imc < 18:
    print("Vinicius Neves" , imc)

elif imc >= 18.5 and imc <= 24.9:
    print("Guilherme Dias" , imc)

elif imc >= 25 and imc <=29.9:
    print("Gabriel Bassani" , imc)

elif imc >= 30 and imc <= 34.9:
    print("Gustavo Tomaz" , imc)

elif imc >= 35 and imc <= 39.9:
    print("Glauber Rodrigo" , imc)

else:
    print("Joel + Claudia + Berenguel + Sandra + Anderson" , imc)