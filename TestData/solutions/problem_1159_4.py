class Solution:
def solution_1159_4(self, nums: List[int]) -> int:
    
    MOD = 10**9 + 7
    n = len(nums)
    for i in range(1,n):
        nums[i]+=nums[i-1]
    
    res,j,k = 0,0,0
    for i in range(n-2):
        if j<=i:
            j = i+1
        while j<n-1 and nums[i]>nums[j]-nums[i]:
            j+=1
        
		if k<j:
            k = j
        while k<n-1 and nums[k]-nums[i]<=nums[n-1]-nums[k]:
            k += 1
        res = (res + k - j)%MOD
    
    return res