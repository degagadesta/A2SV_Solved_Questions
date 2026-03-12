class Node :
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.temp = self.head
    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.temp.next = newNode
        newNode.prev = self.temp
        self.temp = newNode 
    
    def back(self, steps: int) -> str:
        while self.temp.prev and steps :
            self.temp = self.temp.prev
            steps -= 1
        return self.temp.val    
        
    def forward(self, steps: int) -> str:
        while  self.temp.next and steps :
            steps -= 1
            self.temp = self.temp.next
        return self.temp.val    
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)