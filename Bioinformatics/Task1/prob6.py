#Rosalind prob6

myFile = open("prob6.txt", "r")
pattern = myFile.readline().strip()
text = myFile.readline().strip()
mismatch = int(myFile.readline())
myFile.close()

lockPos = []
def hammingDistance(s1, s2):
    "Calculate the hamming distance between two strings"
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

for i in range(len(text)-len(pattern)+1):
    kmer = text[i:i+len(pattern)]
    if (hammingDistance(pattern, kmer)) <= mismatch:
        lockPos.append(i)

print(' '.join(map(str, lockPos)))
