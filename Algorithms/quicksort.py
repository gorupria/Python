#author @Purushot

class QuickSort:

    def __init__(self, input_array):
        self.input_array = input_array
        self.p = 0
        self.r = len(input_array)-1 

    def quicksort(self, arr, p, r):
        if p < r:
            q = self.partition(arr, p, r)
            self.quicksort(arr, p, q-1)
            self.quicksort(arr, q+1, r)

    def partition(self, arr, p, r):
        pivot = arr[r]
        i = p - 1 
        for j in range(p, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1


