class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0 for _ in range(self.capacity)]
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        return self.array[self.length]

        
    def resize(self) -> None:
        self.capacity *= 2
        self.array = [
            self.array[i] 
            if self.length > i and self.array[i]
            else 0
            for i in range(self.capacity) ]

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity