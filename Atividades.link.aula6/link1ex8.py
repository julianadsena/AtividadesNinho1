#Write a Python program to count the number of characters (character frequency) in a string.
palavra = 'google.com'
dict = {}
for i in palavra:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(str(dict))