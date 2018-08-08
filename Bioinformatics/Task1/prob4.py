#rosaling prob4

myFile = open('prob4.txt', 'r')
text = myFile.readline().strip()
clump = myFile.readline().strip()
myFile.close()

clump = list(clump.split())
clump = list(map(int, clump))#converting list of string to int
k = clump[0]
t = clump[2]

def getAllWindow():
    allWindow = []
    for i in range(0, len(text)):
        windows = text[i:i+clump[1]]
        if len(windows) == clump[1]:
            allWindow.append(windows)
    return allWindow

my_dict = {}
result = []
for i in range(len(getAllWindow())):
    currentWindow = getAllWindow()[i]
    j = 0
    for j in range(len(currentWindow)-k+1):
        kmer = currentWindow[j:j+k]
        if kmer in my_dict:
            my_dict[kmer] += 1
        else:
            my_dict[kmer] = 1

    for keys in my_dict:
        if my_dict[keys] == t:
            result.append(keys)
    my_dict.clear()

print(' '.join(sorted(list(set(result)))))




