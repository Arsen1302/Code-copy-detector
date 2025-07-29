class Solution:
    def solution_184_1(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return []

        # since we are doing a "subset" question
        # sorting does not make any differences
        nums.sort()
        n = len(nums)

        # initilization
        # f[i] represents the size of LDS ended with nums[i]
        f = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                # since we have already sorted,
                # then nums[j] % nums[i] will never equals zero
                # unless nums[i] == nums[j]
                if nums[i] % nums[j] == 0:
                    f[i] = max(f[i], f[j] + 1)

        # extract result from dp array
        max_size = max(f)
        max_idx = f.index(max_size) # since we can return one of the largest
        prev_num, prev_size = nums[max_idx], f[max_idx]
        res = [prev_num]
        for curr_idx in range(max_idx, -1, -1):
            if prev_num % nums[curr_idx] == 0 and f[curr_idx] == prev_size - 1:
                # update
                res.append(nums[curr_idx])
                prev_num = nums[curr_idx]
                prev_size = f[curr_idx]

        return res[::-1]