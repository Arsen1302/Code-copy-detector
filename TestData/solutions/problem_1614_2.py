class Solution:
                                    # Because only one of any type can be filled per second,
                                    # the min cannot be less than the max(amount)-- see Ex 1.

                                    # The min also cannot be less than ceil(sum(amount)/2)--see Ex 2.
                                    
                                    # The min cannot be greater than both of these two
                                    # quantities, so... tada

    def solution_1614_2(self, amount: List[int]) -> int:
        return max(max(amount), ceil(sum(amount)/2))