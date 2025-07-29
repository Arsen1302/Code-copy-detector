class Solution:
    def solution_1701_3(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        res=0
        numseven=[]
        numsodd=[]
        targeteven=[]
        targetodd=[]
        for i in nums:
            if i%2==0:
                numseven.append(i)
            else:
                numsodd.append(i)
                
        for i in target:
            if i%2==0:
                targeteven.append(i)
            else:
                targetodd.append(i)
        
        for i in range(len(numseven)):
            if numseven[i]-targeteven[i]>0:
                res+=numseven[i]-targeteven[i]
                
        for i in range(len(numsodd)):
            if numsodd[i]-targetodd[i]>0:
                res+=numsodd[i]-targetodd[i]
        return res//2