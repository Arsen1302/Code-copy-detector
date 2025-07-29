class Solution:
    def solution_1366_3(self, word: str, ch: str) -> str:
        a=''
        if ch not in word:
            return word
        x,c=0,0
        for i in range(len(word)):
            #print(word[i])
            if word[i]==ch:
                x=c    
                #print(x)
                a+=word[i]
                break
            else:
                c+=1
                a+=word[i]
        
        a=a[::-1]
        #print(a)
        for i in range(x+1,len(word)):
            a+=word[i]
        #print(a)
        return a