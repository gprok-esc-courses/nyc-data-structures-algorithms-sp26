
class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.max_size = 10

    def hash_value(self, value):
        return value % self.size
    
    def add(self, value):
        hash = self.hash_value(value)
        if self.data[hash] is None:
            self.data[hash] = [value] 
        else:
            self.data[hash].append(value)
        # if the data[hash] contains max_size elements -> Resize

    def display(self):
        for row in self.data:
            print(row)

    def is_in_table(self, value):
        hash = self.hash_value(value)
        if self.data[hash] is None:
            return False
        if value in self.data[hash]:
            return True
        else:
            return False
        
    def resize(self):
        pass



values = [67, 89, 10, 56, 37, 91, 109, 100, 43, 12, 206]
ht = HashTable(10)
for v in values:
    ht.add(v) 

ht.display()
print(ht.is_in_table(304)) # False
print(ht.is_in_table(56))  # True
print(ht.is_in_table(76))  # False
