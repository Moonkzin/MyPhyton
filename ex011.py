#Crie um programa que recebe altura e largura de uma parede, calcule sua área e a quantidade de tinta necessária
# para pintar, sabendo que cada litro de tinta pinta um area de 2m²

altura = float(input('Informar altura da parede em metros'))
largura = float(input('Informar largura da parede em metros'))

area =float(altura * largura)
tintaLitros = float(area/2)

print('Para pintar sua parede de {} metros de altura e {} metros de largura, que tem {} metros quadrados'
      ' seram necessários {} litros de tinta'.format(altura, largura, area, tintaLitros))