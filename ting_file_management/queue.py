class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def search(self, index):
        if len(self.data) > index >= 0:
            return self.data[index]

        raise IndexError
