class Solution:
    def solution_1331_5(self, n: int) -> bool:
        #check if exactly 1 divisor exists apart from 1 and number itself
        if n <= 3:
            return False
        count = 0
        for i in range(2,n//2 + 1):
            #print(i)
            if n % i == 0:
                count += 1
            if count > 1:
                return False
        if count == 0:
            return False
        return True