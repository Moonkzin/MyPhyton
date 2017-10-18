#faça um algoritmo que receba o salário de um funcionário e informe o salário com 155 de almento

salario = float(input('informar salário'))
salarioComAumento = float(salario+(salario*(15/100)))

print('O seu salário de {} R$ com 15% de almento vai para {:.3f} R$'.format(salario, salarioComAumento))