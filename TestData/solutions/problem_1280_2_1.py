class Solution:
    def solution_1280_2_1(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        mapping = {
            'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'
        }
        
        def solution_1280_2_2(s):
            nonlocal mapping
            return int(''.join(list(map((lambda i:mapping[i]),list(s)))))
        
        return solution_1280_2_2(firstWord) + solution_1280_2_2(secondWord) == solution_1280_2_2(targetWord)