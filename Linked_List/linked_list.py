# Node represents each element in the linked list
class Node:
    def __init__(self, data, next):
        self.data = data   # stores the value
        self.next = next   # pointer to the next node


# LinkedList manages the nodes
class LinkedList:
    def __init__(self):
        self.head = None   # initially list is empty

    # Insert a new node at the beginning (O(1))
    def insert_at_beginning(self, data):
        node = Node(data, self.head)  # new node points to old head
        self.head = node              # update head

    # Insert a new node at the end (O(n))
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)  # if list empty, new node is head
            return

        itr = self.head
        while itr.next:    # move to last node
            itr = itr.next

        itr.next = Node(data, None)  # attach new node at the end

    # Insert a new node at a given index (O(n))
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:   # node before target index
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # Remove a node at a given index (O(n))
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next   # move head to 2nd node
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:   # node before the one to delete
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    # Get the length of the linked list (O(n))
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Print the linked list (O(n))
    def print(self):
        if self.head is None:
            print("(empty)")
            return

        itr = self.head
        llstr = ''
        while itr:
            suffix = '-->' if itr.next else ''
            llstr += str(itr.data) + suffix
            itr = itr.next
        print(llstr)


# ---------------- DRIVER CODE ----------------
if __name__ == '__main__':
    root = LinkedList()

    # Insert at end
    root.insert_at_end(5)
    root.insert_at_end(898)

    # Insert at beginning
    root.insert_at_beginning(77)

    # Insert at specific index
    root.insert_at(1, 99)      # between 77 and 5
    root.insert_at(4, 1000)    # at end

    # Print
    root.print()               # Output: 77-->99-->5-->898-->1000

    # Length
    print("Length:", root.get_length())  # Output: 5

    # Remove operations
    root.remove_at(0)   # remove 77 (head)
    root.remove_at(2)   # remove 898
    root.print()        # Output: 99-->5-->1000
    print("Length:", root.get_length())  # Output: 3
