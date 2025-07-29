class Solution:
    def solution_1433_1(self, digits: List[int]) -> List[int]:
        ans = set()
        for x, y, z in permutations(digits, 3): 
            if x != 0 and z &amp; 1 == 0: 
                ans.add(100*x + 10*y + z) 
        return sorted(ans)