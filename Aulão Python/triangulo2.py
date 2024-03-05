
angulo1 = float(input("Entre com o valor do primeiro ângulo: "))
angulo2 = float(input("Entre com o valor do segundo ângulo: "))
angulo3 = float(input("Entre com o valor do terceiro ângulo: "))

if (angulo1 + angulo2 + angulo3 != 180):
    print("Os valores ", angulo1 , angulo2, "e", angulo3, "não formam triângulo")

elif (angulo1 == 90) or (angulo2 == 90) or (angulo3 == 90):
    print("Triângulo retangulo")

elif (angulo2 < 90) and (angulo2 < 90) and (angulo3 < 90):
    print("Triângulo acutângulo")

else:
    print("Triângulo obtusângulo")