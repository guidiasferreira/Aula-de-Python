
numA = float(input("\n Entre com o primeiro número: "))
numB = float(input("\n Entre com o primeiro número: "))
numC = float(input("\n Entre com o primeiro número: "))

if (numA > numB) and (numA > numC):
    print("maior = %d" % numA)

elif (numB > numA) and (numB > numC):
    print("maior = %d" % numB)

else:
    print("maior = %d" % numC)