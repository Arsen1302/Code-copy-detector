class Solution:
    def solution_365_2(self, nums: List[List[int]]) -> List[int]:
        h = [] # min heap, keeps track of current range that fits 1+ numbers from all lists
        lower, upper = float('inf'), float('-inf') # min and max of the current range

        # initialize current range
        for i, l in enumerate(nums):
            heapq.heappush(h, (l[0], i, 0)) # num, list index, element index
            lower, upper = min(lower, l[0]), max(upper, l[0])
        res = [lower, upper]

        while True:

            # pop smallest element in current range
            num, i, j = heapq.heappop(h)

            # exhausted all elements from the list of the popped element
            if j+1 == len(nums[i]):
                break

            # add the next element from the list of the popped element
            heapq.heappush(h, (nums[i][j+1], i, j+1))

            # get min and max of the new current range
            lower, upper = h[0][0], max(upper, nums[i][j+1])

            # update range if the current range is smaller
            if upper - lower < res[1] - res[0]:
                res = [lower, upper]

        return res