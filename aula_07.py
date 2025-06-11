# import random
# valorGerado = 0

# while(valorGerado != 3):
#     valorGerado = random.randint(0, 10)
#     if(valorGerado == 3):
#         print("Programa encerrado!")
#     else:
#         print("Valor: ", valorGerado)
        
    
    
    #A população de paranavaí é de 95500
    #A população de maringá é de 404000
    # A população de Paranavaí cresce 5% ao ano e de maringá cresce 2% ano. Quantos anos levará para que a população de paranavaí seja maior que a de maringá
    
paranavai = 95500
maringa = 409657
cont = 0

while(paranavai <= maringa):
    paranavai = paranavai * 1.05
    maringa = maringa * 1.02
    cont += 1
    print("Levará ", cont, " anos para Paranavai ser maior que Maringá!")
    
    
    
    
    
    
    
    