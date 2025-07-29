class Solution:
    
    def solution_1447_5_1(self, arr):
        n = len(arr)
        dp = ['None']*n
        dp[0] = arr[0]
        j= 0 
        for i in range(1,n):
            if arr[i]>=dp[j]:
                dp[j+1] = arr[i]
                j+=1
            else:
                idx = bisect.bisect(dp,arr[i],0,j) # log(n)
                dp[idx] = arr[i]
        count = 0
        for i in dp:
            if i=='None':
                break
            count+=1
        return count

        
    def solution_1447_5_2(self, arr: List[int], k: int) -> int:
        ans = 0
        n  = len(arr)
        for i in range(k):
            nums = []
            for j in range(i,n,k):
                nums.append(arr[j])
            ans+=(len(nums)-self.solution_1447_5_1(nums))
            
        return ans