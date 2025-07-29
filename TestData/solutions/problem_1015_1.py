class Solution:
    
    def solution_1015_1(self, nums: List[int]) -> int:
        
        n = len(nums)
        # If nums are less than 3 all can be replace,
        # so min diff will be 0, which is default condition
        if n > 3:
            
            # Init min difference
            min_diff = float("inf")
            
            # sort the array
            nums = sorted(nums)
            
            # Get the window size, this indicates, if we
            # remove 3 element in an array how many element
            # are left, consider 0 as the index, window
            # size should be (n-3), but for array starting
            # with 0 it should be ((n-1)-3)
            window = (n-1)-3
            
            # Run through the entire array slinding the
            # window and calculating minimum difference
            # between the first and the last element of
            # that window
            for i in range(n):
                if i+window >= n:
                    break
                else:
                    min_diff = min(nums[i+window]-nums[i], min_diff)
                    
            # return calculated minimum difference
            return min_diff
        
        return 0 # default condition