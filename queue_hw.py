"""
1. Setup: A queue of people ["Alice","Bob","Charlie"].
2. Goal: Show the order in which people are served.
3. Logic: 
    New arrival: A new person (David) joins the line. Add them to the queue
    
    Serve: The person at the front buys a ticket and leaves. 
    Remove them from the queue and print 'name has bought a ticket'.
    
    Repeat until the line is empty.
"""

class Queue:
    def __init__(self):
        self.queue=["Alice","Bob","Charlie"]
        
    def is_empty(self):
        if len(self.queue) > 0:
            return False
        
        return True
    
    def enqueue(self, item):
        print(f"{item} has joined the line.\n")
        self.queue.append(item) 
        
    def dequeue(self):
        if not self.is_empty():
            print(f"{self.queue[0]} has bought a ticket.")
            self.queue.pop(0)
            
    def size(self):
        return len(self.queue)
            
q=Queue()
q.enqueue("David")

for i in range(0, q.size()):
    q.dequeue()