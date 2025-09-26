nome = input("digite seu nome:  ")
produto = input("qual o produto:  ")
quantidade = int(input(" digite a quantidade:  "))
preco_unitario = float(input(" qual o preco:  "))
Valor_total = quantidade * preco_unitario
print("resumo", nome, produto, quantidade, preco_unitario, Valor_total)