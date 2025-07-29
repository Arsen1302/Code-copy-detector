class Solution:
    def solution_955_4(self, nums: List[int], k: int) -> int:
        max_dq = deque()
        max_sum = float('-inf')

        for i in range(len(nums)):
            local_max = nums[i]
            local_max += max_dq[0][1] if max_dq else 0
            
            max_sum = max(max_sum, local_max)
            
            while max_dq and max_dq[-1][1] < local_max:
                max_dq.pop()
            
			# max_dq can be empty. In this case, the new coming candidate is the new coming number itself
            if local_max > 0:
                max_dq.append((i, local_max))
            
			# remove updated element
            if max_dq and max_dq[0][0] == i-k:
                max_dq.popleft()
            
        return max_sum