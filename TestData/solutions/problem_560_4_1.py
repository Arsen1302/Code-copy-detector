class Solution:
    def solution_560_4_1(self, arr: List[int]) -> int:
        n = len(arr)
        m = arr[-1]
        
        
        def solution_560_4_2(a, index, last2, last):
            if index>=n or last2>m:
                return 0
            if a<2:
                return max(1+solution_560_4_2(a+1,index+1,last2+arr[index],arr[index]), solution_560_4_2(a, index+1, last2, last))
            else:
                pos = bisect_left(arr, last2, lo = index)
                if pos<n and arr[pos]==last2:
                    return (1+solution_560_4_2(a+1,pos+1,last+arr[pos],arr[pos]))
                else:
                    return 0
        
        a=  solution_560_4_2(0,0,0,0)
        if a <3:
            return 0
        else:
            return a