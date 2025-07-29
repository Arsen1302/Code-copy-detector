class Solution:
    def solution_939_4(self, stoneValue: List[int]) -> str:
        take1 = [0 for _ in range(len(stoneValue))]
        take2 = [0 for _ in range(len(stoneValue))]
        take3 = [0 for _ in range(len(stoneValue))]
        skip1 = [0 for _ in range(len(stoneValue))]
        skip2 = [0 for _ in range(len(stoneValue))]
        skip3 = [0 for _ in range(len(stoneValue))]
        
        for i in range(len(stoneValue)-1, -1, -1):
            if i  < len(stoneValue) - 1:
                take1[i] = stoneValue[i] + min(skip1[i+1], skip2[i+1], skip3[i+1])
                take2[i] = stoneValue[i] + take1[i+1]
                take3[i] = stoneValue[i] + take2[i+1]
                skip1[i] = max(take1[i+1], take2[i+1], take3[i+1])
                skip2[i] = skip1[i+1]
                skip3[i] = skip2[i+1]
            else:
                take1[i] = stoneValue[i]
                take2[i] = stoneValue[i]
                take3[i] = stoneValue[i]
                skip1[i] = 0
                skip2[i] = 0
                skip3[i] = 0
        score = max(take1[0], take2[0], take3[0])
        total = sum(stoneValue)
        if score > total - score:
            return 'Alice'
        elif score == total - score:
            return 'Tie'
        else:
            return 'Bob'