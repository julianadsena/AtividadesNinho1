#Crie um programa que receba uma senha de no minimo 4 digitos e  no maximo 8, utilizando somente numeros. 
# O programa deve repetir ate o usuario gerar uma senha valida
#####SOLUÇÃO 1#####
# while (True):
#     senha = input('Digite a senha:')
#     if (senha.isnumeric()):
#         if (len(senha)>4) and (len(senha)<8):
#             print("Sua senha é válida!")
#             break       
#         else:
#             print(f'Sua senha tem {len(senha)} digitos. Digite uma senha entre 4 e 8 dígitos')
#     else:
#         print('Você não digitou uma senha com números')
#---------------------------------------------------------------------------------------------------------
#não é recomendado usar variável global quando não precisa 
####SOLUÇÃO 2#####
def digiteSenha(senha):
    if (senha.isnumeric()):
        if (len(senha)>4) and (len(senha)<8):            
            global repetir
            repetir = False    
            return "Sua senha é válida!"           
        else:
            return(f'Sua senha tem {len(senha)} digitos. Digite uma senha entre 4 e 8 dígitos')
    else:
        return('Você não digitou uma senha com números')
repetir = True
while repetir:
    s =  input('Digite a senha:')
    print(digiteSenha(s))