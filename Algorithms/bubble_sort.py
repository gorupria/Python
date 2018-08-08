#author @Purushot

class BubbleSort:

    def __init__(self, input_array):
        self.input_array = input_array

    def bubble_sort(self):
        print ("Bubble sort is starting...") 
        j = len(self.input_array)-1
        while (j > 1):
            flag = -1
            for i in range(j):
                if self.input_array[i] > self.input_array[i+1]:
                    self.input_array[i], self.input_array[i+1] = self.input_array[i+1], self.input_array[i]
                    flag = self.input_array[i+1]
            print( self.input_array)
            i += 1
            if(flag and flag > 0): 
                j = (self.input_array).index(flag)
            else:
                j = -1
