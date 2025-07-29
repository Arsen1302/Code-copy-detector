class Solution:
    def solution_1491_5(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n=len(nums)
        ans=float('inf')
        oddFreq=Counter([nums[i] for i in range(n) if i%2!=0])
        evenFreq=Counter([nums[i] for i in range(n) if i%2==0])
        evenPos,oddPos=(n+1)//2,n//2
        evenArray=sorted([[key,value] for key,value in evenFreq.items()],key=lambda x:x[1],reverse=True)
        oddArray=sorted([[key,value] for key,value in oddFreq.items()],key=lambda x:x[1],reverse=True)
        if evenArray[0][0]==oddArray[0][0]:
            if len(oddArray)>1:
                ans=min(ans,evenPos-evenArray[0][1]+oddPos-oddArray[1][1])
            else:
                ans=min(ans,evenPos-evenArray[0][1]+oddArray[0][1])
            if len(evenArray)>1:
                ans=min(ans,oddPos-oddArray[0][1]+evenPos-evenArray[1][1])
            else:
                ans=min(ans,oddPos-oddArray[0][1]+evenArray[0][1])
        else:
            ans=min(ans,evenPos-evenArray[0][1]+oddPos-oddArray[0][1])
        return ans