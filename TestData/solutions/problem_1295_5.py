class Solution:
def solution_1295_5(self, triplets: List[List[int]], target: List[int]) -> bool:
    
    curr=[0]*3
    for t in triplets:
        tmp=[max(curr[i],t[i]) for i in range(3)]
        
        f=0
        for i in range(3):
            if tmp[i]>target[i]:
                f=1
                break
        #if all tmp element is less then or equal to target element
        if f==0:
            curr=tmp
            if curr==target:
                return True
    
    return False