class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.size = k
        self.cnt = 0
        self.head = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.cnt < self.size:
            newNode = Node(value)
            if self.isEmpty():
                self.head = self.rear = newNode
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            self.cnt += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.cnt < self.size:
            newNode = Node(value)
            if self.isEmpty():
                self.head = self.rear = newNode
            else:
                self.rear.next = newNode
                newNode.prev = self.rear
                self.rear = newNode
            self.cnt += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            if self.cnt == 1:
                self.head = self.rear = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.cnt -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            if self.cnt == 1:
                self.head = self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
            self.cnt -= 1
            return True
        return False

    def getFront(self) -> int:
        return self.head.val if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.rear.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()