class Solution:
    def solution_729_1(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # a sliding window approach
        currsum = 0
        # first store the sum as if the owner has no super power
        for i in range(len(grumpy)):
            if not grumpy[i]:
                currsum += customers[i]
        
        # now assuming he has the power, take the first window 
        # and add to the previous sum
        for i in range(X):
            if grumpy[i]:
                currsum += customers[i]
        
        maxsum = currsum
        
        # Now the sliding window starts
        # i and j are the two opposite ends of the window
        i = 0
        j = X
        while j < len(customers):
            if grumpy[j]:
                currsum += customers[j]
            if grumpy[i]:
                currsum -= customers[i]
			# we subtract above as the window has already passed over that customer
            if currsum > maxsum:
                maxsum = currsum
            i += 1
            j += 1
        return maxsum