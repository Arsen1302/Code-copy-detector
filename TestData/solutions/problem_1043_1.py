class Solution:
    def solution_1043_1(self, nums: List[int], target: int) -> int:
        ans = prefix = 0
        seen = set([0]) #prefix sum seen so far ()
        for i, x in enumerate(nums): 
            prefix += x
            if prefix - target in seen:
                ans += 1
                seen.clear() #reset seen
            seen.add(prefix)
        return ans