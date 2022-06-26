class NullElementException(Exception):
    """Raise when value is NULL"""

class EmptyStackException(Exception):
    """Raised when stack is empty"""


class Stack:

    def __init__(self, stack=None):
        if(stack==None):
            self.stack = list()
        elif(type(stack)==list):
            self.stack = stack

    def size(self):
        return len(self.stack)

    def push(self, element):
        try:
            if(element == None or element == ''):
                raise NullElementException("Value should not be Null")
            self.stack.append(element)
        except NullElementException as e:
           return e

    def pop(self):
        try:
            if(len(self.stack) == 0):
                raise EmptyStackException("Stack is empty")
            return self.stack.pop()
        except EmptyStackException as e:
             return e

    def peak(self):
        try:
            if(len(self.stack) == 0):
                raise EmptyStackException("Stack is empty")
            return self.stack[-1]
        except EmptyStackException as e:
             return e

    def isEmpty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False
