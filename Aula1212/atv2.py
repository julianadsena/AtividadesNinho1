#Crie uma função que determine se a letra escolhida existe na palavra
def funcao(palavra,letra):
    if (letra in palavra):
        print(f'A letra {letra} está na palavra {palavra}')
    else:
        print('A letra não existe na palavra')
palavra1 = input('Escreva uma palavra:') 
letra1 = input('Escreva uma letra para verificar:')
funcao(palavra1.lower(),letra1.lower())
            
