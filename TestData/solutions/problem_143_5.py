class Solution:
    # O(n+m) runtime;
# O(n+m) space; where n is the string present in pattern 
# and m is the string present in the string
# runtime: 26ms 96.19%
    def solution_143_5(self, pattern: str, string: str) -> bool:
        patternMap = dict()
        stringMap = dict()

        stringList = string.split(" ")
        if len(stringList) != len(pattern):
            return False


        for char, word in zip(pattern, stringList):
            if char in patternMap and patternMap[char] != word:
                return False
            if word in stringMap and stringMap[word] != char:
                return False

            patternMap[char] = word
            stringMap[word] = char

        return True