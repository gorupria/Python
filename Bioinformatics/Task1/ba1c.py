#Rosalind problem ba1c

myFile = open('rosalind_ba1c.txt', 'r')
text = myFile.readline().strip()
myFile.close()

newText = list(text)
for i in range(0, len(text)):
    if newText[i] == 'A':
        newText[i] = 'T'
    elif newText[i] == 'T':
        newText[i] = 'A'
    elif newText[i] == 'G':
        newText[i] = 'C'
    elif newText[i] == 'C':
        newText[i] = 'G'

newText = list(reversed(newText))

print(''.join(newText))
