class Solution:
    def solution_1295_3(self, triplets: List[List[int]], target: List[int]) -> bool:
        m,n,o=0,0,0
        for i,j,k in triplets:
            if i<=target[0] and j<=target[1] and k<=target[2]:
                m=max(m,i)
                n=max(n,j)
                o=max(o,k)
        return [m,n,o]==target
		```