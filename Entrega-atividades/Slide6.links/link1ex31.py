#Write a Python function that takes two lists and returns True if they have at least one common member.
resultado = False
lista1 = [1,6,3,4,5]
lista2 = [5,6,7,8,9]
nova = []
for i in lista1:
    for x in lista2:
        if i == x:
            resultado = True
            nova.append(i)
print(f'Os números que estão repetidos na lista são {nova}')
           
