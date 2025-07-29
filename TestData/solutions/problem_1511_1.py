class Solution:
    def solution_1511_1(self, nums: List[int], k: int) -> int:
        ans = k*(k+1)//2
        prev = -inf 
        for x in sorted(nums): 
            if prev < x: 
                if x <= k: 
                    k += 1
                    ans += k - x
                else: break
                prev = x
        return ans