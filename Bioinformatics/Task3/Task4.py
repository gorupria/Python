#Rosalind set3 task4

text = []
with open("Task4.txt", "r") as f:
    for line in f:
        text.append(line.strip())
f.close()

for i in range(len(text)):
    text[i] = text[i].split()
    text[i].pop(1)

edges = []
for i in range(len(text)):
    a = text[i][1].split(",")
    for j in range(len(a)):
        edges.append([text[i][0],a[j]])

my_list = []
for edge in edges:
    my_list.append(edge)
    for j in range(len(edges)):
        if edges[0][1] == edges[j][0]:
            my_list.append(edges[j])
print(edges)
