class Stack:

    list_numbers = []

    def __init__(self):
        pass

    def push(self, item):
        return self.list_numbers.append(item)

    def pop(self):
        return self.list_numbers.pop()

    def is_empty(self):
        return len(self.list_numbers) == 0
