class Solution:
    def solution_1403_5(self, arr: List[str], k: int) -> str:
        c = collections.Counter(arr)

        for num in arr:
            if c[num] == 1:
                k -= 1
                
            if k == 0:
                return num
        
        return ""