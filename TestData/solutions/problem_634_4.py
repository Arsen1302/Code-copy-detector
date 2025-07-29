class Solution:
    def solution_634_4(self, words: List[str], order: str) -> bool:
        myOrder={k:v for v,k in enumerate(order)}
        
        for word1,word2 in zip(words,words[1:]):
            p1,p2=0,0
            equalFlag=1 #flip to 0 when the 2 diff letters are found
            while p1<len(word1) and p2<len(word2):
                if word1[p1]==word2[p2]:
                    p1+=1
                    p2+=1                    
                elif myOrder[word2[p2]]<myOrder[word1[p1]]:
                    return False
                elif myOrder[word2[p2]]>myOrder[word1[p1]]:
                    equalFlag=0
                    break
                
            if equalFlag and len(word1)>len(word2): #for cases like {apple,app}
                return False
        return True