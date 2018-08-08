#rosalind set3 task2

text = []
with open("Task2.txt") as f:
    for line in f:
        text.append(line.strip())
f.close()
text.pop()

result = []
result.append(text[0])

for kmer in text:
    a = list(kmer)
    result.append(a.pop())

result.pop(1)

print(''.join(result))
