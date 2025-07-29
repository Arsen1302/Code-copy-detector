class Solution:
    def solution_672_5(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        next = [-1] * n
        t_record = dict()
        for i in range(n - 1, -1, -1):
            if nums[i] in t_record:
                next[i] = t_record[nums[i]]
            t_record[nums[i]] = i

        left = 0
        inside = set()
        for right in range(n):
            inside.add(nums[right])
            while len(inside) > k:
                if next[left] == -1 or next[left] > right:
                    inside.remove(nums[left])
                left += 1
            if len(inside) == k:
                cnt = left
                while next[cnt] != -1 and next[cnt] <= right:
                    cnt += 1
                ans += cnt - left + 1
        return ans