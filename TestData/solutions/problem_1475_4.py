class Solution:
    def solution_1475_4(self, corridor: str) -> int:
        ans = 1
        seats = ii = 0 
        for i, x in enumerate(corridor): 
            if x == 'S': 
                if seats and seats % 2 == 0: ans = ans * (i-ii) % 1_000_000_007
                seats += 1
                ii = i
        return ans if seats and seats % 2 == 0 else 0