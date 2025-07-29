class Solution:
    # optimized prefix sum
    def solution_1378_3(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = math.inf
        topSum = sum(grid[0])
        bottomSum = 0

        for i in range(n):
            topSum -= grid[0][i]
            ans = min(ans, max(topSum, bottomSum))
            bottomSum += grid[1][i]

        return ans

    # neetcode's prefix sum method
    def solution_1378_3(self, grid: List[List[int]]) -> int:
        res = float('inf') # max value
        prefixSum1 = [grid[0][0]]
        prefixSum2 = [grid[1][0]] # has the first value done so that we can iterate more smoothly
        length = len(grid[0])

        for i in range(1, length): # from 1 to end because we don't want to deal with an out of bounds error
            prefixSum1.append(grid[0][i] + prefixSum1[i-1]) # doing it this way bc it seems faster but you really just want to calculate the prefix sums of each row and save it to the index
            prefixSum2.append(grid[1][i] + prefixSum2[i-1])
        for i in range(length): # so here we want to calculate the turning point of the first robot
            # calculate the values excluding the current index
            top_row = prefixSum1[-1] - prefixSum1[i] # so total - the current index (which is the accumulated value of the left side, index inclusive)
            bottom_row = prefixSum2[i-1] if i > 0 else 0 # bounds checking here bc 0-1 is -1 and that is not the right place to be.
            current = max(top_row, bottom_row) # take the max values of this index that the second robot can grab
            res = min(res, current) # the first robot is a bad robot so we want to take the minimum values of all the maxes that we calculate and this here is O(1) space complexity instead of saving it all to an array. In taking the minimum, we take thus maximize robot 1's take and robot 2's take per the properties.
        return res



    # simple solution (runs out of time due to not storing the calculations)
    def solution_1378_3(self, grid: List[List[int]]) -> int:

        # this is the simpler code but it doesn't work because of a time limit problem. simply having the prefix sum's already calculated makes this problem ultra efficient
        res = float('inf') # max
        length = len(grid[0])
        for i in range(length): # check each index of the array
            # take the sum of everything after the index on the top row and before the index on the bottom row
            top = sum(grid[0][i+1:])
            bot = sum(grid[1][:i])
            current = max(top, bot) # max of robot 2's take if robot 1 were to turn at this specific index
            res = min(res, current) # determines robot 2's real take that would maximize robot 1's take
        return res