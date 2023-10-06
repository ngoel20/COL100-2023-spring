class Stack:
    def __init__(self):
        # Initialize the stack's data attributes
        self.data = []

    def push(self, item):
        # Push an item to the stack
        self.data.append(item)

    def peek(self):
        # Return the element at the top of the stack
        # Return a string "Error" if stack is empty
        if self.is_empty() == False:
            return self.data[-1]
        else:
            return None

    def pop(self):
        # Pop an item from the stack if non-empty
        if len(self.data) >= 1:
            self.data.pop()
        else:
            print("Stack already Empty")

    def is_empty(self):
        # Return True if stack is empty, False otherwise
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        # Return a string containing elements of current stack in top-to-bottom order, separated by spaces
        # Example, if we push "2" and then "3" to the stack (and don't pop any elements),
        # then the string returned should be "3 2"
        temp = self.data[:]
        temp.reverse()
        ans = ""
        for i in range(len(temp)):
            ans += str(temp[i])
            ans += " "
        return ans

    def __len__(self):
        # Return current number of elements in the stack
        return len(self.data)