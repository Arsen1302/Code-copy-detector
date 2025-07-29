class Solution:
    def solution_995_5(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)

        count = dict(sorted(count.items(), key = lambda x:x[1]))
        ans = len(count)
        for key in count:
            if count[key] <= k:
                ans -=1
                k -= count[key]
        return ans