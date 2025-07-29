class Solution:
    def solution_229_4(self, nums: List[int]) -> int:
        mask, maximum = 0, 0
        for i in range(31, -1, -1):
            mask = mask | 1 << i
            # finding elements having 1's between their msb to ith bit from the start
            # eg: when i = 3 then mask is 11111111111111111111111111111000 , num is 11010
            # then the element added to set will be 11000
            prefixPartSet = { mask &amp; num for num in nums }

            # checking possibility of forming a number having 1 at the i position in current max.
            # eg: current maximum is 101000 and i = 1 so we're checking if 101010 can be formed or not.
            checkingPossibilityOfObtaining = maximum | 1 << i
            for prefix in prefixPartSet:
                # suppose i = 1 and prefix = 111110 and number we want to obtain is = 111010
                # a ^ b = c  - here a = prefix, b = unknow, c = number we want to obtain
                # if b is in the prefixPartSet then it means that number we want to obtain is obtainable
                if checkingPossibilityOfObtaining ^ prefix in prefixPartSet:
                    maximum = checkingPossibilityOfObtaining
                    break
        return maximum