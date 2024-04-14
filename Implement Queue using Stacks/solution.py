class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class MyStack(object):

    def __init__(self):
        self.head = None        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """
        :rtype: int
        """
        if self.head is None:
            return None
        x = self.head.data
        self.head = self.head.next
        return x

    def top(self):
        """
        :rtype: int
        """
        if self.head is None:
            return None
        return self.head.data

    def empty(self):
        """
        :rtype: bool
        """
        return self.head is None

class MyQueue(object):

    def __init__(self):
        self.stack1 = MyStack()
        self.stack2 = MyStack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.top()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack1.empty() and self.stack2.empty()