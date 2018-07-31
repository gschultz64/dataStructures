
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        # Adds a new Node to the end of the list
        node = Node(data)
        if (self.head == None):
            # The list is empty
            self.head = node
        else:
            current = self.head
            while (current.next_node != None):
                current = current.next_node
            current.next_node = node

    def print_list(self):
        if (self.head != None):
            current = self.head
            print(self.head.data)
            while (current.next_node != None):
                current = current.next_node
                print(current.data)

    def delete(self, data):
        # Find the Node to delete (the one with the provided data)
        if (self.head == None):
            return False
        current = self.head
        if (current.data == data):
            # we need to delete the head Node
            temp_node = current.next_node
            current.next_node = None
            self.head = temp_node
        else:
            # we need to keep looping to find the data
            while (current.next_node != None):
                previous = current
                current = current.next_node
                if (current.data == data):
                    temp_node = current.next_node
                    previous.next_node = temp_node
                    current.next_node = None
                    return True
            return False

    def insert_before(self, n, data):
        node = Node(data)
        if (n == 0):
            # insert before the head
            temp_node = self.head
            self.head = node
            self.head.next_node = temp_node
        else:
            current = self.head
            for i in range(0, n):
                previous = current
                current = current.next_node
                if (current == None):
                    previous.next_node = node
                    return True
            temp_node = previous.next_node
            previous.next_node = node
            node.next_node = temp_node

    def get(self, n):
        if (self.head):
            if (n == 0):
                return self.head.data
            else:
                current = self.head.next_node
                i = 1
                while (current.next_node != None and i < n):
                    current = current.next_node
                    i += 1
                if (i == n):
                    return current.data
                else:
                    return None
        else:
            return None

    def delete_at(self, n):
        if (self.head):
            if (n == 0):
                # we need to delete the head Node
                temp_node = self.head.next_node
                self.head.next_node = None
                self.head = temp_node
            else:
                # we need to keep looping to find the Node
                current = self.head.next_node
                i = 1
                while (current.next_node != None and i < n):
                    previous = current
                    current = current.next_node
                    i += 1
                if (i == n):
                    previous.next_node = current.next_node
                    current.next_node = None
                    return True
                else:
                    return False
        else:
            return False

    def enqueue(self, data):
        node = Node(data)
        if (self.head == None):
            self.head = node
        else:
            current = self.head
            self.head = node
            node.next_node = current

    def dequeue(self):
        if (self.head == None):
            return None
        else:
            current = self.head
            after = current.next_node
            while (after.next_node != None):
                current = after
                after = current.next_node
            current.next_node = None
            return after.data


ll = LinkedList()
# ll.enqueue("one")
# ll.enqueue("two")
# ll.enqueue("three")
# ll.enqueue("four")
# ll.enqueue("five")
# ll.print_list()

# ll.add("one")
# ll.add("two")
# ll.add("three")
# ll.print_list()

# print("Dequeueing a single element")
# print(ll.dequeue())
# print(ll.get(5))
# ll.print_list()
# ll.delete_at(1)
# ll.print_list()


class Queue:
    def __init__(self):
        self.store = LinkedList()

    def enqueue(self, data):
        self.store.add(data)

    def dequeue(self):
        data = self.store.get(0)
        self.store.delete_at(0)
        return data


class Stack:
    def __init__(self):
        self.store = LinkedList()

    def push(self, data):
        self.store.insert_before(0, data)

    def pop(self):
        data = self.store.get(0)
        self.store.delete_at(0)
        return data


s = Stack()
s.push("one")
s.push("two")
s.store.print_list()
print(s.pop())

q = Queue()
q.enqueue("first")
q.enqueue("second")
q.store.print_list()
print(q.dequeue())
