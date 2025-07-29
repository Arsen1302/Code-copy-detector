class Solution:
    def solution_929_5(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans = float("-inf")
        for k,v in count.items():
            if k == v:
                ans = max(ans,k)
        return -1 if ans == float("-inf") else ans