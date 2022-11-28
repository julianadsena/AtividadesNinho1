"""Write a Python program to count the number of strings where the string length is 2 or more and the first
 and last character are same from a given list of strings. Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 """
s = 0
lista = ['abc', 'xyz', 'aba', '1221']
for x in lista:
    if len(x)>1 and x[0] == x[-1]:
        s = s + 1
        print('A palavras são',x)
print('numero de palavras:',s) 

