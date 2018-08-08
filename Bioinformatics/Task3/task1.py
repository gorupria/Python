#Rosalind set3 Task1

myFile = open("task1.txt", "r")
k = int(myFile.readline())
text = myFile.readline().strip()
myFile.close()

kmer_list = []

for i in range(len(text)-k+1):
    kmer = text[i:(i+k)]
    kmer_list.append(kmer)

for kmer in (sorted(kmer_list)):
    print(kmer)

