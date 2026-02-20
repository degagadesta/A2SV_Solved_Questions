class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        index = max(arr) - 1
        res = []
        while index > 0:
                temp = arr.index(index+1) + 1
                arr[:temp] = arr[:temp][::-1]
                res.append(temp)

                arr[:index+1] = arr[:index + 1][::-1]
                res.append(index+1)

                if arr[index] == index + 1 :
                    index -= 1

        return res        

        
