class Solution:
    def solution_1422_3(self, colors: List[int]) -> int:
        clr1=colors[0]
        clr2=colors[-1]
        mx=0
        for i in range(len(colors)-1,-1,-1):
            if clr1!=colors[i]:
                mx=max(mx,i)
                break
        for i in range(len(colors)):
            if clr2!=colors[i]:
                mx=max(mx,len(colors)-i-1)
        return mx