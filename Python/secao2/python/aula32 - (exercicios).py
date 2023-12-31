"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""




''' Modo do Angel'''
# Entrada, o usuário vai digitar um número
# number = input('Digite um número: ')

# O código começará a converter o "número" para inteiro (Se o número digitado não for inteiro, ocorrerá uma EXCEÇÃO[erro] e pulará para a linha "except")
# try:
#     number_int = int(number)

#     if number_int % 2 == 0:
#         print(f'O número {number_int} que você digitou é par')
#     else:
#         print(f'O número {number_int} que você digitou é ímpar!')

# except:
#     print('O que você digitou não é um número')



''' Método isdigit'''
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto =' par '

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')


''' Método Try and Except '''
# try:
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto =' par '

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')





"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


''' Angel Método '''

# hora = input(f'Que horas são? (0-24): ')

# horai = int(hora)

# manha = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# tarde = [12, 13, 14, 15, 16, 17]
# noite = [18, 19, 20, 21, 22, 23]

# print(type(horai))

# if horai in manha:
#     print('Bom dia!')
# elif horai in tarde:
#     print('Boa tarde!')
# elif horai in noite:
#     print('Boa noite!')
# elif horai == 24:
#     print('Boa madrugada')
# else:
#     print('Isso não é um horário.')

# # O problema deste código, é que se digitar alguma string ou letra, iria dar erro. a 

''' Udemy'''
# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia!')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Não conheço essa hora!')
# except:
#     print('Por favor, digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""


# Funciona perfeitamente!
nome = input('Insira seu nome, mortal: ')
nomei = len(nome)

nomestr = int(nomei)

if nomestr > 0 and nomestr <= 4:
    print('Nome pequeno')
elif nomestr >= 5 and nomestr <= 6:
    print('Nome normal')
elif nomestr > 6:
    print('Seu nome é grande!')
else:
    print('Definitivamente um dos nomes já criados!')