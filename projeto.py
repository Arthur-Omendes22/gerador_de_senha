import random

letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'
simbolos = '!@#$%^&*_()'

todos_os_caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

tamanho = int(input("Quantos caracteres você quer na senha? "))

senha =''

for i in range(tamanho):
    caractere_aleatorio =random.choice(todos_os_caracteres)
    senha +=caractere_aleatorio

print("Sua senha gerada é", senha)