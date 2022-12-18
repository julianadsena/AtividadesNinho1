#Write a Python program to find the most common elements and their counts of a specified text
from collections import Counter
l = str(input('Digite uma palavra:'))
print('Palavra original' + l)
print('Os elementos mais comuns são', Counter(l).most_common(3))