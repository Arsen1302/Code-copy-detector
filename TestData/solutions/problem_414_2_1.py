class Solution(object):
    def solution_414_2_1(self, nums, k):
        target = sum(nums)
        if target % k != 0: return False
        target //= k
        cur = [0] * k; nums.sort( reverse = True)
        def solution_414_2_2( index):
            if index == len( nums): return True
            for i in range( k):
                if nums[index] + cur[i] <= target:
                    cur[i] += nums[index]
                    if solution_414_2_2( index + 1) == True: return True
                    cur[i] -= nums[index]
                if cur[i] == 0: break
            return False
        return solution_414_2_2( 0)