# Rosalind problem BA1B

infile = open("rosalind_ba1b.txt", "r")
text = infile.readline().strip()
k = int(infile.readline())
infile.close()
n = len(text)

my_dict = {}
for pos in range(n-k+1):
	kmer = text[pos:pos+k]
	if kmer in my_dict:
		my_dict[kmer] += 1
	else:
		my_dict[kmer] =  1
max_count = 0
for key in my_dict:
	if my_dict[key] > max_count:
		max_count =  my_dict[key]
result = []
for key in my_dict:
	if my_dict[key] == max_count:
                result.append(key)
print ' '.join(sorted(result))
