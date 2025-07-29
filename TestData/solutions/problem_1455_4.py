class Solution:
    def solution_1455_4(self, nums: List[int]) -> List[int]:
        half_len_nums = len(nums) // 2
        cnt = Counter(nums)
        keys = sorted(cnt.keys())
        min_key = keys[0]
        diffs = [diff for i in range(1, len(keys))
                 if not (diff := keys[i] - min_key) % 2]
        for d in diffs:
            ans = []
            cnt_copy = cnt.copy()
            for k in keys:
                if cnt_copy[k]:
                    if k + d in cnt_copy and cnt_copy[k] <= cnt_copy[k + d]:
                        ans.extend([k + d // 2] * cnt_copy[k])
                        cnt_copy[k + d] -= cnt_copy[k]
                    else:
                        break
                if len(ans) == half_len_nums:
                    return ans
        return []