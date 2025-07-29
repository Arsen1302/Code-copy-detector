class Solution:
    def solution_734_5(self, arr1: List[int], arr2: List[int]) -> List[int]:
        x = reduce(lambda x, y: x*(-2) + y, arr1)
        x += reduce(lambda x, y: x*(-2) + y, arr2)
        ans = []
        while x: 
            ans.append(x &amp; 1)
            x = -(x >> 1)
        return ans[::-1] or [0]