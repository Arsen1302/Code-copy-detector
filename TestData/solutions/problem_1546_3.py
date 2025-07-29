class Solution:
    def solution_1546_3(self, tasks: List[int]) -> int:
        d=Counter(tasks)
        c=0
		""" If any task is present only once it cannot be completed"""
        for v in d.values():
            if v==1:
                return -1
        
        for k,v in d.items():
            if v==2 or v==3:
                c+=1
            elif v>3:
                c+=math.ceil(v/3)
        return c
		
Please upvote if you find this helpful