class Solution:
    def solution_995_1(self, arr: List[int], k: int) -> int:

        count = Counter(arr)
        ans = len(count)
        for i in sorted(count.values()):
            k -= i
            if k < 0:
                break
            ans -= 1
        return ans