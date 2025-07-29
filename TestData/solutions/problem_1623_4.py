class Solution:
    def solution_1623_4(self, rolls: List[int], k: int) -> int:
        ans = 1
        seen = set()
        for x in rolls: 
            seen.add(x)
            if len(seen) == k: 
                ans += 1
                seen.clear()
        return ans