#author @Purushot

class LongestIncreasingSubSequence():

    def __init__(self, input_array):
        self.input_array = input_array
        self.length = len(input_array)

    def create_dynamic_table(self):
        temp_array = [1] * self.length
        i, j = 1, 0
        while(i < self.length):
            while(j < i and i < self.length):
                if(self.input_array[j] < self.input_array[i] and temp_array[i] < temp_array[j]+1):
                    temp_array[i] += 1
                    j += 1
                else:
                    if(j == i-1):
                        j = 0
                        i += 1
                    else:
                        j += 1
            i += 1
            j = 0

        return temp_array 

    def backtrack_func(self, temp_array):
        result = {} 
        counter = 0
        for item in temp_array:
            counter += 1
            result[item] = counter-1 

        print("The length of LSI is: " + str(len(result)))
        print("The Longest Increasing Sequence is:")
        for key, val in result.items():
            print(self.input_array[val], end=" ")

