class Solution:
    POW = 397
    MODULO = 100000000069
    def solution_1559_3(self, nums: List[int], k: int, p: int) -> int:
        arr = list(map(lambda x: 1 if x % p == 0 else 0, nums))
        ans_set = set[int]()
        for i in range(len(arr)):
            cnt_one = 0
            hash1 = 0
            for j in range(i, len(arr)):
                hash1 = (hash1 * Solution.POW + nums[j] + (j + 1 - i)) % Solution.MODULO
                if arr[j] == 1:
                    cnt_one += 1
                if cnt_one <= k:
                    ans_set.add(hash1)
                else:
                    break

        return len(ans_set)