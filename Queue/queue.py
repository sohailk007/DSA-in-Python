# Implementing a Queue in Python
# There are several ways to implement a queue in Python:

# Method 1: Using Python List

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Dequeue from empty queue")
    
    def peek(self):
        """Return the front item without removing it"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty queue")
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def __str__(self):
        """Return string representation of the queue"""
        return f"Queue({self.items})"

# Example usage
if __name__ == "__main__":
    queue = Queue()
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(f"After enqueues: {queue}")  # Queue([10, 20, 30])
    
    # Peek at front element
    print(f"Front element: {queue.peek()}")  # 10
    
    # Dequeue elements
    print(f"Dequeued: {queue.dequeue()}")  # 10
    print(f"Dequeued: {queue.dequeue()}")  # 20
    print(f"After dequeues: {queue}")    # Queue([30])
    
    # Check if empty
    print(f"Is empty: {queue.is_empty()}")  # False
    
    # Check size
    print(f"Size: {queue.size()}")  # 1
    
# Method 2: Using collections.deque
# The deque (double-ended queue) from the collections module is optimized for fast appends and pops from both ends.

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Dequeue from empty queue")
    
    def peek(self):
        """Return the front item without removing it"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Peek from empty queue")
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)
    
    def __str__(self):
        """Return string representation of the queue"""
        return f"Queue({list(self.items)})"

# Example usage
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue)  # Queue(['a', 'b', 'c'])
print(queue.dequeue())  # 'a'
print(queue)  # Queue(['b', 'c'])


# Method 3: Using queue.Queue
# Python's queue module provides a thread-safe implementation of a queue.

from queue import Queue as ThreadSafeQueue

class Queue:
    def __init__(self):
        self.items = ThreadSafeQueue()
    
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.put(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue"""
        if not self.is_empty():
            return self.items.get()
        raise IndexError("Dequeue from empty queue")
    
    def peek(self):
        """Return the front item without removing it (not natively supported)"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        
        # Create a temporary queue to access elements
        temp = ThreadSafeQueue()
        front_item = None
        
        # Move all items to temporary queue to access the front
        while not self.items.empty():
            item = self.items.get()
            if front_item is None:  # First item we get is the front
                front_item = item
            temp.put(item)
        
        # Restore the original queue
        while not temp.empty():
            self.items.put(temp.get())
            
        return front_item
    
    def is_empty(self):
        """Check if the queue is empty"""
        return self.items.empty()
    
    def size(self):
        """Return the number of items in the queue"""
        return self.items.qsize()
    
    def __str__(self):
        """Return string representation of the queue"""
        # Not straightforward with ThreadSafeQueue, so we'll skip it
        return "Queue (ThreadSafe implementation)"

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(f"Size: {queue.size()}")  # Size: 3
print(f"Front element: {queue.peek()}")  # Front element: 1
print(f"Dequeued: {queue.dequeue()}")  # Dequeued: 1

