#Set 2
#Rosaling problem2

myFile = open("prob2.txt", "r")
k = int(myFile.readline())

seq1 = myFile.readline().strip()
seq2 = myFile.readline().strip()
seq3 = myFile.readline().strip()
seq4 = myFile.readline().strip()
seq5 = myFile.readline().strip()

myFile.close()

def hammingDistance(s1, s2):
    "Calculate the hamming distance between two strings"
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))






