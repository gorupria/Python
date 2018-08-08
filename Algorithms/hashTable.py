#author @Purushot

class HashTable:
    
    def __init__(self):
        self.size = 20
        self.my_array = [None] * self.size

    def put_value(self, my_key, my_value):
        self.my_array[self.myhash(my_key)] = my_value  

    def get_value(self, my_key):
        return self.my_array[self.myhash(my_key)] 

    def myhash(self, key):
        total = 0 
        for item in key:
            total += ord(item)
        return total % self.size

    




