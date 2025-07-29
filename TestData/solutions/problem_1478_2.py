class Solution:
    def solution_1478_2(self, nums: List[int]) -> List[int]:
        dict1=dict()
        l=[]
        for i in nums:
            if(i in dict1.keys()):
                dict1[i]=-1
            else:    
                dict1[i]=1
            dict1[i-1]=-1
            dict1[i+1]=-1    
        for i in nums:
            if(dict1[i]==1):
                l.append(i)
        return l