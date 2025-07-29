class Solution:
    def solution_376_2(self, dictionary: List[str], sentence: str) -> str:
        
        sentence = sentence.split()
        
        operated = []
        
        for word in dictionary :
            k = len(word)
            for i in range(len(sentence)):
                if sentence[i][:k] == word :
                    if i not in operated :
                        sentence[i] = word
                        operated.append(i)
                    else:
                        if len(word) < len(sentence[i]) :
                            sentence[i] = word 
        return " ".join(sentence)