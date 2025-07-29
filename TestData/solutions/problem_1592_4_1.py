class Solution:
    def solution_1592_4_1(self, cookies: List[int], k: int) -> int:
        bag=[0]*k
        self.ans=float('inf')
        self.solution_1592_4_2(cookies,bag,0,k)
        return self.ans
    def solution_1592_4_2(self,cookies,bag,start,k):
        if max(bag)>self.ans:
            return
        if start>=len(cookies):
            temp=max(bag)
            self.ans=min(self.ans,temp)
            return
        for j in range(k):
            bag[j]+=cookies[start]
            self.solution_1592_4_2(cookies,bag,start+1,k)
            bag[j]-=cookies[start]
        return