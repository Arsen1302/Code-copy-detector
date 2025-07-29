class Solution:
    def solution_1699_4_1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0;j = 0;ans = 0
        
        while(i<n):
            #print(gcd)
            gcd = nums[i]
            for j in range(i,n):
                gcd = solution_1699_4_2(nums[j],gcd)
                if(gcd==k):
                    ans+=1
                elif(gcd<k):
                    break
            i+=1
        return ans
            
            
def solution_1699_4_2(a,b):
    if(b==0):
        return a
    else:
        return solution_1699_4_2(b,a%b)