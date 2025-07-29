class Solution:
    def solution_1403_3(self, arr: List[str], k: int) -> str:
        a =[i for i in arr if arr.count(i)==1];
        return "" if k > len(a) else a[k - 1]