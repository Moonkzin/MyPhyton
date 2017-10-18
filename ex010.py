#crie um programa que pergunte quantos dólares tem na carteira e informe quantos dólares pode comrpar considerando 3,27 o valor do dolar

dinheiro = float(input('Quanto dinheiro vc tem na carteira?'))

dolar = float(dinheiro/3.27)

print('você pode comprar {:.3f} dólares com seus {} reais, já que o dolares vale R$ 3,27'.format(dolar, dinheiro))