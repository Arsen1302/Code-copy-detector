class Solution:
    def solution_1401_4_1(self, parents: List[int]) -> int:
        
        def solution_1401_4_2(n):
            k=1
            for i in child[n]:
                k += solution_1401_4_2(i)
            nums[n]=k
            return k
        
        child = {}
        for i in range(len(parents)):
            child[i]=[]
        for i in range(1,len(parents)):
            child[parents[i]].append(i)
        
        nums={}
        solution_1401_4_2(0)
        k=1
        for i in child[0]:
            k*=nums[i]
        score=[k]
        for i in range(1,len(nums)):
            k=1
            k*=(nums[0]-nums[i])
            for j in child[i]:
                k*=nums[j]
            score.append(k)
            
        return score.count(max(score))