class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        net = defaultdict(int)
        for i in bills:
            if i == 5 :
                net[5] += 1
            elif i == 10:
                if net[5] == 0 :
                    return False
                net[5] -= 1
                net[10] += 1
            else :
                if net[5] >= 1 and net[10] >= 1 :
                    net[5] -= 1
                    net[10] -= 1
                elif net[5] >= 3:
                    net[5] -= 3
                else:
                    return False
        return True                                 
        