#author @Purushot

class MergeSort():

    def __init__(self, input_array):
        self.input_array = input_array
        self.length = len(input_array)

    def merge_sort(self, arr):
        if(len(arr) < 2):
            return arr 
        middle = len(arr)//2 
        left_array = [None] * middle
        right_array = [None] * (len(arr) - middle)
        for i in range(middle):
            left_array[i] = arr[i]

        j = 0
        for i in range(middle, len(arr)):
            right_array[j] = arr[i]
            j += 1

        self.merge_sort(left_array)
        self.merge_sort(right_array)
        self.merge_array(left_array, right_array, arr)

    def merge_array(self, left_array, right_array, arr):
        i = j = k = 0
        while(i < len(left_array) and j < len(right_array)):
            if(left_array[i] <= right_array[j]):
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1

            k += 1

        while(i < len(left_array)):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while (j < len(right_array)):
            arr[k] = right_array[j]
            j += 1
            k += 1
        
