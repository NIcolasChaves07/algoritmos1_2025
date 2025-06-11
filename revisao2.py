# print("1 = Atendimento, 2 - Fazer Pedido, 3 - Suporte, 4 - Sair")
# numSend = int(input("Escolha a sua opção: "))

# while(numSend != 7):
#     if(numSend == 1):
#         print("Estamos te redirecionando para o sistema de atendimento")
#         numSend = int(input("1 - Atendimento, 2 - Fazer Pedido, 3 - Suporte, 4 - Sair: "))
#     elif(numSend == 2):
#         print("Estamos te redirecionando para o sistema de pedidos")
#         numSend = int(input("1 - Atendimento, 2 - Fazer Pedido, 3 - Suporte, 4 - Sair: "))
#     elif(numSend == 3):
#         print("Estamos te redirecionando para o sistema de suporte")
#         numSend = int(input("1 - Atendimento, 2 - Fazer Pedido, 3 - Suporte, 4 - Sair: "))
#     elif(numSend == 4):
#         print("Obrigado(a) pela sua preferência!")
#         break
#     else:
#         print("Parâmetro inválido!")

# import math
# import random

# a = 0
# cont = 0

# while(a != 7):
#     numeroAleatorio = random.randint(1, 10)
#     a = numeroAleatorio + 1
#     print(a)
#     cont = cont + 1
#     print("O código foi repetido: ", cont, " vezes.")

num = int(input("Informe um valor: "))
mult = int(input("Informe o limite inicial de tabuada: "))
fimNum = int(input("Informe o valor final de tabuada: "))
mult2 = None

while(mult <= fimNum):
    mult2 = mult * num
    print(f"{num} x {mult} = {mult2}")
    mult+= 1
  