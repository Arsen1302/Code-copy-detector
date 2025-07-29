class Solution:
#     Runtime: 45ms 94.99% Memory: 14.1mb 22.45%
    def solution_434_4(self, left: int, right: int) -> List[int]:
        if not left and not right:
            return []
        numberRange = list(range(left, right + 1))
        result = []
        for i in numberRange:
            flag = True
            copy = i
            while copy != 0:
                num = copy % 10
                if num == 0 or i % num != 0:
                    flag = False
                    break
                copy //= 10
            if flag:
                result.append(i)

        return result