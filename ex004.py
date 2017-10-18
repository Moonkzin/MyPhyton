# Digite algo no teclado e imprima todas as informações possíveis dele
palavra = input('Digite qualquer coisa')

print('É um número? ', palavra.isnumeric())
print('É letras? ', palavra.isalpha())
print('É Letras e números? ', palavra.isalpha())
print('É tudo maiúsculo? ', palavra.isupper())

