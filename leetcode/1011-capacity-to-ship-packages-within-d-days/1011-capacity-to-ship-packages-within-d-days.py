class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            needed_days = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    needed_days += 1
                    current_load = w
                else:
                    current_load += w
            return needed_days <= days

        left = max(weights) - 1 
        right = sum(weights)
        
        while left + 1 < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid  
            else:
                left = mid   
                
        return right
