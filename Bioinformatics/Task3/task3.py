#Rosalind set3 task3

myFile = open("task3.txt", "r")
k = int(myFile.readline())
text = myFile.readline().strip()
myFile.close()

graph = {}
kmer_list = []
for i in range(len(text)-k+1):
    kmer = text[i:i+k]
    kmer_list.append(kmer)

kmer_list = list(set(kmer_list))
for kmer in kmer_list:
    from_node = kmer[:len(kmer)-1]
    to_node = kmer[1:]

    if from_node in graph:
        graph[from_node].append(to_node)
    else:
        graph[from_node] = [to_node]

for ele in graph.values():
    ele.sort()

for k,v in sorted(graph.items()):
    print(k+' -> '+','.join(v))

