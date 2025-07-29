class Solution:
#     O(n) || O(n)
# Runtime: 323ms 48.44% Memory: 15.7mb 65.00%
    def solution_292_2(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)

        stack = list()

        for i in range(2*len(nums)):

            circularIdx = i % len(nums)

            while len(stack) > 0 and nums[stack[len(stack)-1]] < nums[circularIdx]:
                top = stack.pop()
                result[top] = nums[circularIdx]

            stack.append(circularIdx)

        return result