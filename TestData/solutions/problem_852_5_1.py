class Solution:
    def solution_852_5_1(self, array: List[int]) -> List[int]:
        return self.solution_852_5_2(array)

    #     O(N) || O(1) 133ms 82.42%
    def solution_852_5_2(self, array):
        rightMax = -1
        for i in reversed(range(len(array))):
            maxVal = max(rightMax, array[i])
            array[i] = rightMax
            rightMax = maxVal
        return array
        
    # O(n^2) || O(1) TLE
    def solution_852_5_3(self, array):
        if not array:
            return array
        
        for i in range(len(array)):
            maxVal = 0
            for j in range(i+1, len(array)):
                maxVal = max(maxVal, array[j])
            array[i] = maxVal


        array[-1] = -1

        return array