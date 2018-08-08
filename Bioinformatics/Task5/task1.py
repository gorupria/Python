#Rosaling set5 -> task1

myFile = open("task1.txt", "r")
text = myFile.readline().strip().split()
myFile.close()
text_length = len(text)
text[0] = text[0].replace("(","")
text[text_length -1] = text[text_length - 1].replace(")", "")


for i in range(text_length):
    text[i] = int(text[i])

def reverse_list(input_array):
    input_array.reverse()
    input_array = map(lambda x: -x, input_array)

    return input_array

def sorting_method(main_array):
    result = []
    reversal_distance = 0

    for i in range(text_length):
        if main_array[i] != i+1:
            if i+1 in main_array:
                id_i = main_array.index(abs(i+1))
            else:
                id_i = main_array.index(-abs(i+1))
            main_array[i: id_i +1] = reverse_list(main_array[i: id_i +1])
            reversal_distance += 1
            result.append(main_array[:])
        if main_array[i] == -(i+1):
            main_array[i] = i+1
            result.append(main_array[:])


    return result

result = sorting_method(text)
f = open('result.txt', 'w')
for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] >= 1:
            result[i][j] = '+' + str(result[i][j])
    my_str = " ".join(str(e) for e in result[i])
    f.write("("+ my_str +")")
    print("("+ my_str +")")

f.close()


