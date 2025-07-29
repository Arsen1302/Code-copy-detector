class Solution:
    def solution_9_2(self, x: int) -> bool:
        if x < 0:
            return False
        length, temp = -1, x
        while temp:
            temp = temp // 10
            length += 1
        
        temp = x
        while temp:
            left, right = temp // 10**length, temp % 10
            if left != right:
                return False
            temp = (temp % 10**length) // 10
            length -= 2
        return True