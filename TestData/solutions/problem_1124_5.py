class Solution:
    def solution_1124_5(self, nums: List[int]) -> int:

        # we can make an array where we save the prefix sum
        # for every even and odd number
        even = 0
        odd = 0

        # save the prefix sums
        for idx, num in enumerate(nums):

            # check whether we are odd or even
            if idx % 2:  # odd
                nums[idx] = odd + num
                odd = nums[idx]
            else:
                nums[idx] = even + num
                even = nums[idx]

        # initialize the result
        result = 0
        
        # now delete every single element
        for idx, num in enumerate(nums):
            if idx % 2:  # odd index
                
                # in order to construct the even sum
                # we need the following:
                # 
                # The even sum from before this element
                # The odd sum from after this element till the end
                # the second sum corresponds to current prefix sum
                # minus the last odd
                even_sum = nums[idx-1] + odd - nums[idx]

                # for the odd summ we need the following:
                #
                # The odd sum from before this element
                # and the even sum after this element
                # which corresponds to the last even sum
                # minus the sum from the element before this
                #
                # here we need to deal with the special case in
                # the beginning, where idx-2 might not be defined
                if idx == 1:
                    odd_sum = even - nums[idx-1]
                else:
                    odd_sum = nums[idx-2] + even - nums[idx-1]
            else:  # even index

                # in order to construct the even sum we need the
                # following:
                #
                # The even sum from before this element
                # The pdd sum after this element which can be computed
                # using the last odd sum minus the sum right before
                # 
                # we also need to deal with special cases. For the
                # zeros element we don't have anything right before
                if idx == 0:
                    even_sum = odd
                else:
                    even_sum = nums[idx-2] + odd - nums[idx-1]

                
                # in order to construct the odd sum we need the
                # following:
                #
                # The odd sum before this element
                # The even sum after this element, which can be
                # computet with the final even minus the current
                # sum
                if idx == 0:
                    odd_sum = even-nums[idx]
                else:
                    odd_sum = nums[idx-1] + even - nums[idx]
            
            # now check whether the sums are equal
            if odd_sum == even_sum:
                result += 1
        return result