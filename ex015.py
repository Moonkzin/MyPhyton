# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
# pelos quais foi alugado. Calcule o preço a pagar. Sabendo que que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

qdeDias = int(input('Quantos dias o carro foi alugado?'))
qdeKM = float(input('Quantidade de quelometros rodados'))

valorQdedias = qdeDias*60
valorQdeKM = qdeKM*0.15

valorTotal = valorQdedias + valorQdeKM

print('O valor a ser pago pelo alugél do carro é de R$ {}'.format(valorTotal))