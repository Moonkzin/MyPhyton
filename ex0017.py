#Crie um programa que leia os catetos de um triangulo retângulo e mostre o comprimento da hipotenusa

import math

catetoA = float(input('Comprimento do Cateto Adjacente'))
catetoO = float(input('Comprimento do Cateto Oposto'))

hipotenusa = float(math.sqrt(catetoA**2 + catetoO**2))

print('O valor da hipotenusa é {} quando o Cateto Adjacente for {} e o Cateto Oposto for {}.'.format(hipotenusa,
                                                                                                     catetoO, catetoO))