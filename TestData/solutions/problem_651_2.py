class Solution:
    def solution_651_2(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        ans = []

        if x == 1 or y == 1:
            num = max(x, y)
            exponent = 0
            while num**exponent < bound:
                ans.append(num**exponent+1)
                exponent += 1

            if num**exponent == bound:
                ans.append(num**exponent)
            return set(ans)
        
        i, j = 0, 0
        while True:
            ans.append(x**i+y**j)
            j += 1
            if x**i+y**j > bound:
                j = 0
                i += 1
                if x**i+y**j > bound:
                    return set(ans)