class Solution:
    def solution_861_3(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr)+1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]
        return [prefix[lo] ^ prefix[hi+1] for lo, hi in queries]