#Rosalind problem5

infile = open("prob5.txt", "r")
text = infile.readline().strip()
infile.close()

def skew(text):
    result = []
    skew_value = 0
    result.append(skew_value)
    for i in text:
        if i == 'C':
            skew_value -= 1
        if i == "G":
            skew_value += 1
        result.append(skew_value)
    return [str(i) for i, j in enumerate(result) if j == min(result)]

print(' '.join(skew(text)))
