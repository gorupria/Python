#Rosalind ba1d

myFile = open('ba1d.txt', 'r')
comString = list(myFile.readline().strip())
text = list(myFile.readline().strip())
myFile.close()

positionLock = []
for i in range(0, len(text)):
    if comString[0] == text[i]:
        kmer = ''.join(text)[i:i+len(comString)]
        if kmer == ''.join(comString):
            positionLock.append(i)

print(' '.join(str(x) for x in positionLock))#can also be done as print(*positionLock)
