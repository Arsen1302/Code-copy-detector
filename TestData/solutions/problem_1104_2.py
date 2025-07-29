class Solution:
    def solution_1104_2(self, nums: List[int]) -> List[int]:
        lst = sorted([(key, freq) for key, freq in Counter(nums).items()],
                     key=lambda tpl: (tpl[1], -tpl[0]))
        ans = []
        for key, freq in lst:
            ans += [key] * freq
        return ans