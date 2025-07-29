class Solution:
    def solution_512_5(self, sentence: str) -> str:
        vwl_lst = ['a','e','i','o','u','A','E','I','O','U']
        
        sentence = sentence.split()
        
        for i in range(len(sentence)):
            if sentence[i][0] in vwl_lst:
                
                sentence[i] = sentence[i]+"ma"+ ("a"*(i+1))
            else:
                a = sentence[i][0]
                sentence[i] = sentence[i][1:]
                sentence[i] = sentence[i]+a
                sentence[i] = sentence[i]+"ma"+("a"*(i+1))
                
        return ' '.join(sentence)