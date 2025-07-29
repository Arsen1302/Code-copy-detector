class Solution:
    def solution_1258_5_1(self, s: str) -> bool:
        # convert the string into digits.
        s = [int(i) for i in list(s)]
        
        def solution_1258_5_2(base, index, nums):
			## increment power of 10. 
            d = 0
			## accumulate the value for 10. 
            acc = 0
            res = False
			## check the value from reverse from the index -1 where we calculated base.
            for x in range(index,-1,-1):
                acc += (10**d)*nums[x]

                if base + 1 == acc:
                    if x-1 >= 0:
						## collect recursion output
                        res = res or solution_1258_5_2(acc, x-1, s)
                    else:
                        res = True
                d+=1
            return res
                
        d = 0
        ans = False
        acc = 0
        ## same logic as recursion - just driver outside the recusion function. 
		## The logic below could possibly also be included ithe same recursion solution with some effort. 
        for x in range(len(s)-1,-1,-1):
            acc += (10**d)*s[x]
            ans = ans or solution_1258_5_2(acc, x-1, s)
            d+=1
        return ans