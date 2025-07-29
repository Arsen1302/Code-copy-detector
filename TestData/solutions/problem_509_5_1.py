class Solution:
    def solution_509_5_1(self, string: str, char: str) -> List[int]:
        return self.solution_509_5_2(string, char)
#     O(n) || O(n)
# Runtime: 53ms 78.92% Memory: 13.9mb 91.60%
    def solution_509_5_2(self, string, char):
        n = len(string)
        leftArray, rightArray, result = ([float('inf')] * n, 
                                         [float('inf')] * n, 
                                         [float('inf')] * n)
        temp = float('inf')
        for i in range(len(string)):
            if string[i] == char:
                temp = 0
            leftArray[i] = temp
            temp += 1

        temp = float('inf')
        for i in reversed(range(len(string))):
            if string[i] == char:
                temp = 0
            rightArray[i] = temp
            temp += 1


        for i in range(len(result)):
            result[i] = min(leftArray[i], rightArray[i])

        return result

    
#     O(n^2) || O(n) Runtime: TLE
    def solution_509_5_3(self, string, char):
        sequence = [float('inf')] * len(string)
        newList = []
        for idx, val in enumerate(string):
            if val == char:
                newList.append(idx)

        for val1 in newList:
            for idx2, val2 in enumerate(string):
                sequence[idx2] = min(sequence[idx2], abs(idx2-val1))

        return sequence