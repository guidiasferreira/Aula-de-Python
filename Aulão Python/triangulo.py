
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 >= lado2 + lado3) or (lado2 >= lado1 + lado3) or (lado3 >= lado1 +lado2):
    print("Os valores " , lado1 ,"", lado2 ,"", lado3,  "Não formam um triângulo")

elif (lado1 == lado2) and (lado2 == lado3):
    print("Triângulo equilátero")

elif (lado1 != lado2) and (lado1 != lado3) and (lado2 < lado3):
    print("Triângulo escaleno")

else:
    print("Triângulo isoceles")