
faturamento = 1200
custo = 770
novas_vendas = 300
taxa_imposto = 0.1
teve_lucro = True

faturamento = faturamento + novas_vendas

mensagem = ("O faturamento foi de " , faturamento)

imposto = taxa_imposto * faturamento

print("Faturamento" , faturamento)
print("Custo" , custo)
print("Lucro" , faturamento - custo - imposto)
print(mensagem,)