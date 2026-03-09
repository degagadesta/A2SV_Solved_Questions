class DataStream:

    def __init__(self, value: int, k: int):
        self.que = deque()
        self.value = value
        self.k = k
        self.cnt = 0
        
    def consec(self, num: int) -> bool:
        self.que.append(num)
        if num == self.value :
            self.cnt += 1
        if len(self.que) > self.k :
            temp = self.que.popleft()
            if temp == self.value :
                self.cnt -= 1
        return self.cnt == self.k        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)