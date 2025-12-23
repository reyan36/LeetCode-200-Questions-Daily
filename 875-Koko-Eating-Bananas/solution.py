class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
 
            if not self.can_eat(piles , mid, h):
                left = mid + 1
            else:
                right = mid
        
        return left

    def can_eat(self , piles , speed , h):
        hours = 0

        for pile in piles:
            if speed >= pile:
                hours += 1
            else:
                hours += math.ceil(pile / speed) 
            
        return hours <= h
            