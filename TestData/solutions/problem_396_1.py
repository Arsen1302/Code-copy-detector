class Solution:
    def solution_396_1(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        ct = [1] * len(nums)
        maxLen, maxCt = 0, 0
        
        # same as the LIS code, iterate
        # over all the elements once and then
        # from 0 -> i again to compute LISs
        for i in range(len(nums)):
            for j in range(i):
                # If it's a valid LIS
                if nums[i] > nums[j]:
                    # and if the length
                    # of LIS at i wrt j
                    # is going to be increased
                    # update the length dp
                    # and since this is just one
                    # continous LIS, count of i
                    # will become same as that of j
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j] + 1
                        ct[i] = ct[j]
                    # if on the other hand, the
                    # length of the LIS at i becomes
                    # the same as it was, it means
                    # there's another LIS of this same
                    # length, in this case, add the LIS
                    # count of j to i, because the current
                    # LIS count at i consists of ways to get
                    # to this LIS from another path, and now
                    # we're at a new path, so sum thse up
                    # there's no point
                    # in updating the length LIS here.
                    elif dp[i] == dp[j] + 1:
                        ct[i] += ct[j]
            
            # at any point, keep track
            # of the maxLen and maxCt
            # we'll use it to compute our result
            if dp[i] > maxLen:
                maxLen = dp[i]
                
        # now, we have the maxLength
        # of the given nums, we can iterate
        # over all 3 arrays (hypothetically)
        # and just add up the count of all those
        # LIS which are the longest (maxLen)
        # and that's the result
        for i in range(len(nums)):
            if maxLen == dp[i]:
                maxCt += ct[i]
    
 
        return maxCt