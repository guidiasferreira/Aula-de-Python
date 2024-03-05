
cargo = input("Entre com o cargo do funcionário: ")
salario = float(input("Entre com o salário atual: "))

if cargo == "gerente":
    aumento = salario * 0.1

elif cargo == "tecnólogo":
    aumento = salario * 0.2

else:
    aumento = salario * 0.25

novoSalario = salario + aumento

print("O", cargo, "tinha salário igual: \t \t" , salario)
print("Teve aumento de: \t \t \t" , aumento)
print("E passou a ganhar: \t \t \t" , novoSalario)

   