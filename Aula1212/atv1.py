#Crie uma função para comparar o tamanho de duas palavras. 
# Essa função vai receber duas palavras e vai determinar qual das duas é a maior e imprimir na tela
def TamPalavra(palavra1,palavra2):
    if len(palavra1)>len(palavra2):
        print(f'A palavra {palavra1} ({len(palavra1)} letras) é a maior que a {palavra2}({len(palavra2)} letras)')
    elif len(palavra1)<len(palavra2):
        print(f'A palavra {palavra2} ({len(palavra2)} letras)é maior que a {palavra1} ({len(palavra1)} letras)')
    elif len(palavra1)==len(palavra2):
        print(f'A palavra {palavra2} ({len(palavra2)} letras) tem o mesmo tamanho que a {palavra1} ({len(palavra1)} letras)')
    else:
        print('Você não digitou uma palavra válida')
n1 = input('Digite uma palavra:')
n2 = input('Digite uma palavra:')
TamPalavra(n1,n2)