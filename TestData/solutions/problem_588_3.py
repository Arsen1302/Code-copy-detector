class Solution:
    def solution_588_3(self, tree: List[int]) -> int:

        tracker = collections.defaultdict(int)
        start = result = 0
        
        for end in range(len(tree)):
            tracker[tree[end]] += 1
            while len(tracker) > 2:
                tracker[tree[start]] -= 1
                if tracker[tree[start]] == 0: del tracker[tree[start]]
                start += 1
            result = max(result, end - start + 1)
        
        return result