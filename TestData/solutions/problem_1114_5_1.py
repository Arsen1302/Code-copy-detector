class Solution:
    def solution_1114_5_1(self, inventory: List[int], orders: int) -> int:
        
        left = 0
        right = max(inventory)
        
        while right - left > 1:
            mid = left + (right - left) // 2
            
            sold_balls = sum(inv - mid for inv in inventory if inv > mid)
            
            if sold_balls > orders:
                left = mid
            
            else:
                right = mid
        
        sold_balls = total = 0
        
        def solution_1114_5_2(val):
            return (val * (val + 1)) // 2
        
        for inv in inventory:
            if inv > right:
                sold_balls += (inv - right)
                total += solution_1114_5_2(inv) - solution_1114_5_2(right)
            
        if sold_balls < orders:
            total += (orders - sold_balls) * right
        
        return total % (10**9 + 7)
		
credit: @EvgenySH