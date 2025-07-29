class Solution:
    def solution_1227_1(self, word: str) -> int:
        
        word = re.findall('(\d+)', word)
        numbers = [int(i) for i in word]
        
        return len(set(numbers))