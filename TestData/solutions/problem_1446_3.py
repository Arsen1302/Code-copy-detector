class Solution:
    def solution_1446_3(self, prices: List[int]) -> int:
        seq, tot = 1, 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] == -1:
                seq += 1
            else:
                tot += seq*(seq+1)/2
                seq = 1
        return int(tot + seq*(seq+1)/2)
		```