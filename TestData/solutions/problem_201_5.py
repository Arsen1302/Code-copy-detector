class Solution:
    def solution_201_5(self, n: int) -> int:
        # explanation
        # F algorithem is take the even index element from the list and reverse the list
        # solution_201_5(9) = F([1, 2, 3, 4, 5, 6, 7, 8, 9])
        # first round: F([2, 4, 6, 8]) = F(2 * [1, 2, 3, 4]) = 2 * F([4, 3, 2, 1])
        # convert F([4, 3, 2, 1]) = F([3, 1])
        # now we need to convert F[(3, 1)] to F([1, 3]), which is the original order then do F algorithm
        # 4 - 4 + 1 = 1
        # 4 - 2 + 1 = 3
        # n//2 - F(n//2) + 1
        # base case is 1
        return 2 * (n // 2 - self.solution_201_5(n//2) + 1) if n != 1 else 1