
# Dynamic Array

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = x
        self.size += 1
        print(f"Appended {x} | Size: {self.size}, Capacity: {self.capacity}")

    def resize(self):
        print("Resizing...")
        self.capacity *= 2
        new_arr = [None] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            return "Underflow"
        val = self.arr[self.size - 1]
        self.size -= 1
        print(f"Popped {val}")
        return val

    def display(self):
        print("Array:", self.arr[:self.size])



# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def insert_end(self, x):
        new = Node(x)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def delete(self, x):
        temp = self.head

        if temp and temp.data == x:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next

        if not temp:
            print("Value not found")
            return

        prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



# Doubly Linked List

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new = DNode(x)
        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new = DNode(x)
                new.next = temp.next
                new.prev = temp

                if temp.next:
                    temp.next.prev = new

                temp.next = new
                return
            temp = temp.next
        print("Target not found")

    def delete_pos(self, pos):
        temp = self.head
        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            if not temp:
                return
            temp = temp.next

        if not temp:
            return

        if temp.next:
            temp.next.prev = temp.prev

        if temp.prev:
            temp.prev.next = temp.next

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")



# Stack using SLL

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return "Underflow"
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.data if self.head else None



# Queue using SLL

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new = Node(x)
        if not self.tail:
            self.head = self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def dequeue(self):
        if not self.head:
            return "Underflow"
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        return self.head.data if self.head else None



# Parentheses Checker

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.pop() != pairs[ch]:
                return False

    return stack.head is None



# MAIN TEST

if __name__ == "__main__":
    print("=== Dynamic Array ===")
    arr = DynamicArray(2)
    for i in range(10):
        arr.append(i)
    arr.display()

    arr.pop()
    arr.pop()
    arr.pop()
    arr.display()

    print("\n=== Singly Linked List ===")
    sll = SinglyLinkedList()
    sll.insert_begin(3)
    sll.insert_begin(2)
    sll.insert_end(5)
    sll.traverse()
    sll.delete(2)
    sll.traverse()

    print("\n=== Doubly Linked List ===")
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_after(2, 99)
    dll.traverse()
    dll.delete_pos(1)
    dll.traverse()

    print("\n=== Stack ===")
    st = Stack()
    st.push(10)
    st.push(20)
    print(st.pop(), st.peek())

    print("\n=== Queue ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue(), q.front())

    print("\n=== Parentheses Checker ===")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(t, "->", is_balanced(t))