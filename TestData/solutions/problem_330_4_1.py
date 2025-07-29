class Solution:
    def solution_330_4_1(self, s: str) -> str:
        reversed_s = ""
        current_word = []
        
        for c in s:
            if c == " ":
                reversed_s += self.solution_330_4_2(current_word) + " "
                current_word = []
            else:
                current_word.append(c)
                
        return reversed_s + self.solution_330_4_2(current_word)
    
    def solution_330_4_2(self, word: List[int]) -> str:
        l, r = 0, len(word) - 1
        
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        
        return "".join(word)