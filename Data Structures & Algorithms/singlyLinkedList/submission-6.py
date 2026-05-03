class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if self.length - 1 < index or index < 0:
            return -1

        currentNode = self.head
        currentIndex = 0

        while currentNode:
            if currentIndex == index:
                return currentNode.value
            currentIndex += 1
            currentNode = currentNode.next
        
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node
        self.length += 1

        if self.length == 1:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = Node(val, None)
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.length += 1        
        
        if self.length == 1:
            self.head = node

    def remove(self, index: int) -> bool:
        if self.length - 1 < index or index < 0:
            return False
        
        currentNode = self.head
        previousNode = None
        currentIndex = 0

        while currentNode:
            if currentIndex == index:
                if index == 0:
                    self.head = self.head.next
                    
                    if self.length == 1:
                        self.tail = None

                elif index == self.length - 1:
                    self.tail = previousNode
                    self.tail.next = None

                else:
                    previousNode.next = currentNode.next
                self.length -= 1
                return True

            currentIndex += 1
            previousNode = currentNode
            currentNode = currentNode.next
        
        return False
            

    def getValues(self) -> List[int]:
        array = []

        currentNode = self.head

        while currentNode:
            array.append(currentNode.value)
            currentNode = currentNode.next

        return array