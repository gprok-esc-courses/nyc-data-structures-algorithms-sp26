
class Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    
    def enqueue(self, value):
        self.data.append(value) 

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.data.pop(0)
        return value 
    

queue = Queue()
queue.enqueue(35)
queue.enqueue(54)
queue.enqueue(16)

value = queue.dequeue()
print(value)

value = queue.dequeue()
print(value)

value = queue.dequeue()
print(value)

value = queue.dequeue()
print(value)