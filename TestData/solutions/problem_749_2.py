class Solution:
    def solution_749_2(self, label: int) -> List[int]:
        
        x = label
        mask = 0 
        while x > 1:
            x >>= 1
            mask <<= 1
            mask |= 1
            
        x = label
        res = deque()
        while x:
            res.appendleft(x)
            x >>= 1
            mask >>= 1
            x ^= mask
        return res