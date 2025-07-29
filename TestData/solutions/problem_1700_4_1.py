class Solution:
    def solution_1700_4_1(self, nums: List[int], cost: List[int]) -> int:
        def solution_1700_4_2(t): #function for calculating cost for Target "t"
            cur = cur_prev = cur_nxt = 0 #initialize the cost counting
            for i, el in enumerate(nums):
                cur += abs(el-t) * cost[i] #update the cost for target "t"
                cur_prev += abs(el-(t-1)) * cost[i] #update the cost for target "t-1"
                cur_nxt += abs(el-(t+1)) * cost[i] #update the cost for target "t+1"
            return cur, cur_prev, cur_nxt
                
        
        l, r = min(nums), max(nums) #lower and upper bound for searching
        ans = float('inf')
        while l <= r:
            m = (l+r) // 2
            cur, cur_prev, cur_nxt = solution_1700_4_2(m) #call the counting function for target "m"
            if cur_prev >= cur <= cur_nxt: #if "m" if efficient than both "m-1" and "m+1" then cost for m is the ans
                return cur
			#update to efficient segment
            if cur_prev > cur_nxt:
                l = m+1
            else:
                r = m-1
        return cur