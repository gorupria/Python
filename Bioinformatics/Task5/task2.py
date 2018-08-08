#Rosaling set5 -> task2

myFile = open("task2.txt", "r")
text = myFile.readline().strip().split()
myFile.close()
text[0] = text[0].replace("(","")
text[len(text) -1] = text[len(text) - 1].replace(")", "")


for i in range(len(text)):
    text[i] = int(text[i])

text = [0] + text
text.append(abs(text[-1] + 1))

flag = False
breakpoint_array = []
for i in range(len(text)-1):
    if (text[i+1] - text[i]) != 1:
        if flag == True:
            flag = False
        else:
            breakpoint_array.append(text[i])

    if text[i+1] - text[i] == 1:
        if flag == False:
            breakpoint_array.append([text[i]] + [text[i+1]])
        if flag == True:
            breakpoint_array[-1].append(text[i+1])
        flag = True

print(len(breakpoint_array)-1)
