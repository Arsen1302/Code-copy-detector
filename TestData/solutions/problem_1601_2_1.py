class Solution:
    def solution_1601_2_1(self, n: int) -> int:
        mod = 1_000_000_007
        # edge case
        if n == 1: return 6
        # to create possible adjacent pairs
        next_option = {
            1: (2, 3, 4, 5, 6),
            2: (1, 3, 5),
            3: (1, 2, 4, 5),
            4: (1, 3, 5),
            5: (1, 2, 3, 4, 6),
            6: (1, 5)
        }
        # create dictionary where the key is allowed adjacent pairs and the value is list of third elment after the pair
        allowed_third = defaultdict(list)
        for i, j, k in product(list(range(1, 7)), repeat=3):
            if k != i and j in next_option[i] and k in next_option[j]:
                allowed_third[(i, j)] += k,
        # memoize the answers
        @cache
        def solution_1601_2_2(i, j, rem):
            ans = 0
            if rem == 0:
                return 1
            for k in allowed_third[(i, j)]:
                ans += solution_1601_2_2(j, k, rem - 1) % mod
            return ans
        ans = 0
        
        for i, j in allowed_third:
            ans += solution_1601_2_2(i, j, n - 2) % mod
        return ans % mod