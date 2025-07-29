class Solution:
    def solution_389_3(self, nums: List[int]) -> bool:
        is_modified = False         # to check for multiple occurances of False condition(non increasing)
        index = -1                  # to get the index of false condition
        n = len(nums)
        if n==1:return True
        for i in range(1, n):
            if nums[i] < nums[i-1] and not is_modified:      # check if nums[i-1] is greater than nums[i]
                index = i                                    # stores the index
                is_modified = True                           # mark the change which is to be modified
            elif nums[i] < nums[i-1] and is_modified:        # if another false occurs return false (atmost 1 false cond.)
                return False
        if index != -1:
            v = nums[index-1]
            nums[index-1] = nums[index]                      # modifying index value and check for sort
            idx = index-1
            if idx-1>=0 and idx<n and nums[idx-1]<=nums[idx]<=nums[idx+1]:   # check if modified array is sorted or not
                return True
            elif idx==0 and idx+1<n and nums[idx]<=nums[idx+1]:              # check if modified array is sorted or not
                return True
            nums[index-1]=v
            nums[index] = nums[index-1]+1
            if index-1>=0 and index+1<n and nums[index-1]<=nums[index]<=nums[index+1]:     # check if modified array is sorted or not
                return True
            elif index==n-1 and nums[index-1]<=nums[index]:
                return True
        if index==-1:                        # if array is already sorted
            return True
        return False