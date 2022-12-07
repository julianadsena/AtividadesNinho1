#escreva uma palavra e escolha uma letra. Retorne o número de vezes que a letra aparece
def checarLetra(palavra,letra):
    contador = 0
                    # SOLUÇÃO NUMERO 1
    # for i in range(len(palavra)):  
    #     if (palavra[i]==letra):
    #         contador += 1
    # return contador 
    for caractere in palavra:
        if (caractere == letra):
            contador +=1
    return contador
palavraEsc = input('Escreva uma palavra:') 
letraEsc = input('Escreva uma letra para verificar:')
print(checarLetra(palavraEsc.lower(),letraEsc.lower()))
                    #SOLUÇÃO NÚMERO 2
# print(palavra.lower().count(letra.lower()))
