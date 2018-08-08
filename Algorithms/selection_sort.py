#auther @Purushot

class SelectionSort:

    def __init__(self, input_array):
        self.input_array = input_array
        self.length = len(input_array)

    def selection_sort(self):
        for i in range(self.length-1):
            for j in range(self.length-i-1):
                current_item = self.input_array[j+i] if self.input_array[j+i] < self.input_array[j+i+1] else self.input_array[j+i+1]
                j += 1
            self.input_array.remove(current_item) 
            self.input_array.insert(i, current_item)
            i += 1
            print(self.input_array)
