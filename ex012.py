#Faça um algoritmo que leia o preço de um produto e motre seu novo preço com 5% de desconto

preco = float(input('informe o preço que quer saber quanto fica com desconto'))
precoComDesconto = float(preco-(preco*(5/100)))

print('O valor {} R$ com 5 % de desconto é {}'.format(preco, precoComDesconto))