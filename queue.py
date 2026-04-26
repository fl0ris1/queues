class Queue:
    def __init__(self):
        self.queue=[]
        
    def is_empty(self):
        if len(self.queue)==0:
            return True
        
        return False
    
    def enqueue(self,item):
        self.queue.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
           return IndexError("No Values Availible")
       
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        
        return IndexError("No Values Availble")
    
    def rear(self):
        if not self.is_empty():
            return self.queue[-1]
        
        return IndexError("No Values Availbile")
    
    def display(self):
        if not self.is_empty():
            return self.queue
        
        return IndexError("No Values Availble")
    
    
if __name__=="__main__":
    q=Queue()
    q.enqueue(3)
    q.enqueue(6)
    q.enqueue(9)
    
    print(q.display())
    q.dequeue()
    print(q.size())
    print(q.peek())
    q.dequeue()
    q.dequeue()
    print(q.display())
