class Solution:
    def solution_1491_4(self, nums: List[int]) -> int:

        # trivial case
        if len(nums) < 2:
            return 0
        
        # count the even and odd indexed numbers
        cn_even = collections.Counter(nums[::2])
        cn_odd = collections.Counter(nums[1::2])

        # use the most common even and odd index numbers if they are not equal
        most_even = cn_even.most_common(2)
        most_odd = cn_odd.most_common(2)

        # check whether most common elements are equal and if so
        # check out which combination is better
        if most_even[0][0] == most_odd[0][0]:

            # if both have two most common elements
            if len(most_even) == 2 and len(most_odd) == 2:

                # get the subtractor for the case where both have multiple different
                # elements and find the combination that has the most characters
                # that need no changing
                subtractor = max(most_even[0][1] + most_odd[1][1], most_even[1][1] + most_odd[0][1])
            elif len(most_even) == 2:

                # we need to take 
                subtractor = most_odd[0][1] + most_even[1][1]
            elif len(most_odd) == 2:
                subtractor = most_odd[1][1] + most_even[0][1]
            else:
                subtractor = len(nums) - len(nums)//2
        else:
            subtractor = most_even[0][1] + most_odd[0][1]

        return len(nums) - subtractor