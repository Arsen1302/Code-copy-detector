class Solution:
    def solution_1618_4(self, nums: List[int]) -> int:
        ans = -1
        seen = {}
        for x in nums: 
            sm = sum(int(d) for d in str(x))
            if sm in seen: 
                ans = max(ans, seen[sm] + x)
                seen[sm] = max(seen[sm], x)
            else: seen[sm] = x
        return ans