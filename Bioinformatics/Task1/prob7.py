#Rosalind prob7
import collections

myFile = open('prob7.txt', 'r')
text = myFile.readline().strip()
digits = myFile.readline().strip()
myFile.close()

digits = list(digits.split())
digits = list(map(int, digits))#converting list of string to int
k = digits[0]
in_mistake = digits[1]
out_result = [];
mismatch_list = []

def hammingDistance(s1, s2):
    "Calculate the hamming distance between two strings"
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

for i in range(len(text)-k+1):
    kmer = text[i:i+k]
    out_result.append(kmer)

for t_kmer in set(out_result):
    for s_kmer in out_result:
        if hammingDistance(t_kmer, s_kmer) <= in_mistake:
            mismatch_list.append(t_kmer)

result = []
frequentKmers = []
mismatch_count = collections.Counter(mismatch_list)
mismatch_count = mismatch_count.most_common()

"""
for i in range(len(mismatch_count)):
    result.append(mismatch_count[i][1])
    a = max(result)
    if mismatch_count[i][1] == a:
        frequentKmers.append(mismatch_count[i][0])

print(' '.join(frequentKmers))
"""
print(mismatch_count.most_common())
