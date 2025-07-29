class Solution:
    def solution_1627_4(self, nums: List[int]) -> int:


        num = set(nums)

        a = list(num)

        a.sort()

        ans = 0

        for i in range(len(a)):
            if a[i] != 0:
                ans += 1

                for j in range(i + 1, len(a)):
                    a[j] -= a[i]
                    
        return ans