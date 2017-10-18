# Crie um programa que converta as temperaturas de Cº p/ fº > fóruma C=5/9.( F-32).

c = float(input('Informe a temperatura de graus Celsios'))

f = float((1.8*c)+(32))

print('A temperatura em {}Cº corresponde a Fº {} '.format(c, f))