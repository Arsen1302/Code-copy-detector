class Solution:
    def solution_672_2(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        latest = {}
        unique = 0
        prev = 0
        for i in range(n):
            if nums[i] not in latest:
                unique += 1
            latest[nums[i]] = i
            if unique > k :
                while True:
                    if latest[nums[prev]] == prev:
                        latest.pop(nums[prev])
                        prev += 1
                        unique -= 1                        
                        break
                    else:
                        prev += 1
                        
            if unique == k:
                ans += 1
                tmp = prev
                while True:
                    if latest[nums[tmp]] != tmp:
                        ans += 1
                        tmp += 1
                    else:
                        break
        return ans