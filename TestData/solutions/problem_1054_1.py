class Solution:
    def solution_1054_1(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        sum = 0
        for i in range(1,len(piles)-int(len(piles)/3),2):
            sum += piles[i]
            print(sum)
        return sum