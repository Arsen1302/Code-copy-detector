class Solution:
    def solution_991_4(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)-1):
            flag=False
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    ans.append(abs(prices[i]-prices[j]))
                    flag=True
                    break
            if flag==False:
                ans.append(prices[i])
    
                
        ans.append(prices[-1])
        return ans