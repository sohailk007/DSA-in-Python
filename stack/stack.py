# Method 1: Using Python List

class Stack:
    
    def __init__(self):
        self.items = []
        
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        """Return the top item without removing it"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def __str__(self):
        """Return string representation of the stack"""
        return f"Stack({self.items})"

# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(f"After pushes: {stack}")  # Stack([10, 20, 30])
    
    # Peek at top element
    print(f"Top element: {stack.peek()}")  # 30
    
    # Pop elements
    print(f"Popped: {stack.pop()}")  # 30
    print(f"Popped: {stack.pop()}")  # 20
    print(f"After pops: {stack}")    # Stack([10])
    
    # Check if empty
    print(f"Is empty: {stack.is_empty()}")  # False
    
    # Check size
    print(f"Size: {stack.size()}")  # 1
    
   
# Method 2: Using collections.deque
# The deque (double-ended queue) from the collections module is optimized for fast appends and pops from both ends.
     
from collections import deque

class Stack:
    def __init__(self):
        self.items = deque()
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        """Return the top item without removing it"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)
    
    def __str__(self):
        """Return string representation of the stack"""
        return f"Stack({list(self.items)})"

# Example usage
stack = Stack()
stack.push('a')
stack.push('b')
stack.push('c')
print(stack)  # Stack(['a', 'b', 'c'])
print(stack.pop())  # 'c'
print(stack)  # Stack(['a', 'b'])


# Method 3: Using queue.LifoQueue
# Python's queue module provides a thread-safe implementation of a stack.

from queue import LifoQueue

class Stack:
    def __init__(self):
        self.items = LifoQueue()
    
    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.put(item)
    
    def pop(self):
        """Remove and return the top item from the stack"""
        if not self.is_empty():
            return self.items.get()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        """Return the top item without removing it (not natively supported)"""
        # LifoQueue doesn't have a peek method, so we need to implement it
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        
        # Temporary storage
        temp = LifoQueue()
        top_item = None
        
        # Move all items to temporary queue to access the top
        while not self.items.empty():
            item = self.items.get()
            if top_item is None:  # First item we get is the top
                top_item = item
            temp.put(item)
        
        # Restore the original stack
        while not temp.empty():
            self.items.put(temp.get())
            
        return top_item
    
    def is_empty(self):
        """Check if the stack is empty"""
        return self.items.empty()
    
    def size(self):
        """Return the number of items in the stack"""
        return self.items.qsize()
    
    def __str__(self):
        """Return string representation of the stack"""
        # Not straightforward with LifoQueue, so we'll skip it
        return "Stack (LifoQueue implementation)"

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Size: {stack.size()}")  # Size: 3
print(f"Top element: {stack.peek()}")  # Top element: 3
print(f"Popped: {stack.pop()}")  # Popped: 3