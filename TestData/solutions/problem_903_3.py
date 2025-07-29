class Solution:
    def solution_903_3(self, num: int) -> List[int]:
        # Without Sort
        mini=float('inf')
        res=[]
        for i in range(1,int(sqrt(num+1))+1):
            if (num+1)%i==0:
                if ((num+1)//i)-i<mini:
                    res=[i,(num+1)//i]
                    mini=((num+1)//i)-i
        
        for i in range(1,int(sqrt(num+2))+1):
            if (num+2)%i==0:
                if ((num+2)//i)-i<mini:
                    res=[i,(num+2)//i]
                    mini=((num+2)//i)-i
        return res