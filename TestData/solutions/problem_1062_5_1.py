class Solution:
    def solution_1062_5_1(self, s: str) -> int:

        
        memo = {}
        def solution_1062_5_2(curr_path, s, count):
            if (len(s), count) in memo:
                return memo[(len(s), count)]
            if not s:
                if count == 3:
                    return 1
                return 0

            res = 0
            for i in range(1, len(s) + 1):
                sub_string = s[0 : i]
                if curr_path == None:
                    res += solution_1062_5_2(sub_string.count("1"), s[i : ], count + 1)
                else:
                    if sub_string.count("1") == curr_path:
                        res += solution_1062_5_2(sub_string.count("1"), s[i : ], count + 1)
                    else:
                        continue
            memo[(len(s), count)] = res
            return memo[(len(s), count)]
        L = solution_1062_5_2(None, s, 0)
        return L