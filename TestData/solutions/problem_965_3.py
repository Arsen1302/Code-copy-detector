class Solution:
    def solution_965_3(self, arr: List[int]) -> int:
        n=len(arr)
        count=0
        for i in range(n):
            val=arr[i]
            for j in range(i+1,n):
                val^=arr[j]
                if val==0:
                    count+=j-i
        return count