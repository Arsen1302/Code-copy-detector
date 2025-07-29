class Solution:
    def solution_1664_5(self, s: str) -> int:
        count=0
        x=set()

        for i in s:
            if i in x:
                count+=1
                x=set([i])

            else:
                x.add(i)

        return count+1