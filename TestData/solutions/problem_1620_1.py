class Solution:
                    # From number theory, we know that an integer num divides each
                    # integer in a list if and only if num divides the list's gcd.
                    # 
                    # Our plan here is to:
                    #   • find the gcd of numDivide
                    #   • heapify(nums) and count the popped elements that do not
                    #     divide the gcd.
                    #   • return that count when and if a popped element eventually
                    #     divides the gcd. If that never happens, return -1 
        
    def solution_1620_1(self, nums: List[int], numsDivide: List[int]) -> int:
	
        g, ans = gcd(*numsDivide), 0            # <-- find gcd (using * operator)

        heapify(nums)                           # <-- create heap

        while nums:                             # <-- pop and count

            if not g%heappop(nums): return ans  # <-- found a divisor? return count
            else: ans+= 1                       # <-- if not, increment the count

        return -1                               # <-- no divisors found
		
#--------------------------------------------------
class Solution:    # version w/o heap. Seems to run slower
    def solution_1620_1(self, nums: List[int], numsDivide: List[int]) -> int:
	
        g = gcd(*numsDivide)
        nums.sort()

        for i,num in enumerate(nums):
            if not g%num: return i

        return -1