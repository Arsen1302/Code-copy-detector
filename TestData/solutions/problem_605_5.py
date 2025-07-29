class Solution:
    def solution_605_5(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        res = 0
        c = collections.Counter(arr)
        keys = sorted(c)

        for i, k in enumerate(keys):
            left, right = i, len(keys) - 1
            
            new_target = target - k
            while left <= right:
                left_v, right_v = keys[left], keys[right]
                
                if left_v + right_v < new_target:
                    left += 1
                elif left_v + right_v > new_target:
                    right -= 1
                else:
                    if i < left < right:
                        res += c[k] * c[left_v] * c[right_v]
                    elif i == left and left < right:
                        res += c[k] * (c[k] - 1) // 2 * c[right_v]
                    elif i < left and left == right:
                        res += c[k] * c[left_v] * (c[left_v] - 1) // 2
                    else:
                        res += c[k] * (c[k] - 1) * (c[k] - 2) // 6
                
                    left += 1
                    right -= 1
                
        return res % MOD