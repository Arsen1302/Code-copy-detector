class Solution:
    def solution_1559_5(self, nums, k, p):
        n, seen = len(nums), set()

        for i in range(n):
            s, count = "", 0
            for j in range(i,n):
                if nums[j]%p == 0:
                    count += 1

                if count > k:
                    break 

                s += str(nums[j]) + "#"

                seen.add(s)

        return len(seen)