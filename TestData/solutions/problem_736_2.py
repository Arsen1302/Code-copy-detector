class Solution:
#     Runtime: 43ms 59.41% || Memory: 13.9mb 73.25%
#       O(n) || O(1) if you dont count return result as a extra space
    def solution_736_2(self, string: str, first: str, second: str) -> List[str]:
        result = []
        string = string.split()
        for i in range(len(string) - 2):
            currStr = string[i]
            secNxtStr = string[i + 1]
            thirdNxtStr = string[i + 2]

            if currStr == first and secNxtStr == second:
                result.append(thirdNxtStr)


        return result