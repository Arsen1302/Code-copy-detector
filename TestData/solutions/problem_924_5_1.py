class Solution:
    def solution_924_5_1(self, slices: List[int]) -> int:
        
        def solution_924_5_2(index,end,slices,n,dic):
            key=(index,n)
            if key in dic:
                return dic[key]
            else:
                if n==0 or index>end:
                    return 0
                include=slices[index]+solution_924_5_2(index+2,end,slices,n-1,dic)
                exclude=solution_924_5_2(index+1,end,slices,n,dic)
                dic[key]=max(include,exclude)
                return dic[key]
        l=len(slices)
        dic1={}
        dic2={}
        c1=solution_924_5_2(0,l-2,slices,l//3,dic1)
        c2=solution_924_5_2(1,l-1,slices,l//3,dic2)
        return max(c1,c2)