class Solution:
    def solution_1483_3(self, num: int) -> int:
        list_digits = []
        while num > 0:
            list_digits.append(num % 10)
            num = num // 10
        
        a, b, c, d= sorted(list_digits)
        return 10 * a + c + 10*b + d