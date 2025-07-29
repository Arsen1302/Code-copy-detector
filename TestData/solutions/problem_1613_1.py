class Solution:
    def solution_1613_1(self, nums: List[int], threshold: int) -> int:
                            # Stack elements are the array's indices idx, and montonic with respect to nums[idx].
                            # When the index of the nearest smaller value to nums[idx] comes to the top of the 
                            # stack, we check whether the threshold criterion is satisfied. If so, we are done.
                            #  If not, we continue. Return -1 if we reach the end of nums without a winner.
							
        nums.append(0)
        stack = deque()

        for idx in range(len(nums)):

            while stack and nums[idx] <= nums[stack[-1]]:           
                n = nums[stack.pop()]                               # n is the next smaller value for nums[idx]
                k = idx if not stack else idx - stack[-1] -1        
                if n > threshold //k: return k                      # threshold criterion. if n passes, all
                                                                    # elements of the interval pass
            stack.append(idx)

        return -1