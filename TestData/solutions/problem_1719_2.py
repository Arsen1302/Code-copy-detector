class Solution:
    def solution_1719_2(self, nums, k):
        n, count = len(nums), 0

        for i in range(n):
            temp = nums[i]
            for j in range(i,n):
                temp = math.lcm(temp,nums[j])
                if temp == k:
                    count += 1
                elif temp > k:
                    break

        return count