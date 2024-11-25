# python use an array for stack essentially
stack = []

# Push
stack.append("A")
stack.append("B")
stack.append("C")
print("Stack: ", stack)

# Pop
element = stack.pop()
print("Pop: ", element)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(stack))


# actual class using arrays => Memory Efficient, Easier to implement and understand
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# class Stack using linked lists => Dynamic size
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size


history = []  # Stack to store actions

# Simulating actions
history.append("Type A")
history.append("Type B")
history.append("Delete B")

# Undoing the last action
last_action = history.pop()  # Undo "Delete B"
print(f"Undo action: {last_action}")
