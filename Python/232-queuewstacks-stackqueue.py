class MyQueue:

    def __init__(self):
        self.queue = []
        self.storage_queue = []

    def push(self, x: int) -> None:
        while len(self.queue) != 0: 
            self.storage_queue.append(self.queue.pop())
        self.queue.append(x)
        while len(self.storage_queue) != 0:
            self.queue.append(self.storage_queue.pop())

    def pop(self) -> int:
        return_int = self.queue.pop()
        return return_int

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0