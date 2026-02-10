class RandomizedSet:
    def __init__(self):
        self.randomSet=dict()
        self.temp=dict()
        self.cnt=0
        self.left=0
    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        self.randomSet[val]=self.cnt
        self.temp[self.cnt]=val
        self.cnt+=1
        return True    
    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        index=self.randomSet[val]
        del self.randomSet[val]
        del self.temp[index]
        self.left+=1
        return True  
    def getRandom(self) -> int:
        if len(self.temp)>0:
            return random.choice(list(self.temp.values()))
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
