class Solution:    
    def solution_376_4(self, roots: List[str], sentence: str) -> str:
        sentence = sentence.split()        
        for root in roots:
            for i, word in list(enumerate(sentence)):
                if word.startswith(root):
                    sentence[i] = root        
        return " ".join(c for c in sentence)