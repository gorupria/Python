#Rosalind problem1

myFile = open("task1.txt", "r")
pattern = myFile.readline().strip()
text = myFile.readline().split()
myFile.close()

def hammingDistance(s1, s2):
    "Calculate the hamming distance between two strings"
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

d = []
min_d = []
for i in range(len(text)):
    for j in range(len(text[0])):
            kmer = text[i][j:j+len(pattern)]
            if len(kmer) == len(pattern):
                distance = hammingDistance(pattern, kmer)
                d.append(distance)
            if j == (len(text[0])- 1):
                min_d.append(min(d))
                d = []

print(''.join(str(sum(min_d))))
