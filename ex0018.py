#Faça um programa qualquer que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
# ângulo

import math
angulo = float(input('Informe o Angulo'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Para o angulo {:.2f}° o valor do \n'
      'SENO é {:.2f}, o \n'
      'COSSENO é {:.2f} e a \n'
      'TANGENTE é {:.2f}'. format(angulo, seno, cosseno, tangente))