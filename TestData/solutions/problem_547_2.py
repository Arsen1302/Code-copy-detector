class Solution:
#     O(n) || O(1)
# Runtime: 1159ms 49.65% Memory: 18mb 49.96%
    def solution_547_2(self, bills: List[int]) -> bool:
        fiveBills, tenBills = 0, 0

        for i in bills:
            if i == 5:
                fiveBills += 1
            elif i == 10:
                tenBills += 1
                fiveBills -= 1
            elif tenBills > 0:
                tenBills -= 1
                fiveBills -= 1
            else:
                fiveBills -= 3

            if fiveBills < 0:
                return False


        return True