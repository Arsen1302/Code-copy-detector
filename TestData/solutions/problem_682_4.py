class Solution:
    def solution_682_4(self, words: List[str]) -> List[str]:
        if len(words)==1:
            return list(*words)
        output=[]
        for i in words[0]:
            temp=0
            for j,k in enumerate(words[1:]):
                if i in k:
                    words[j+1]=k.replace(i,"_",1)
                    temp+=1
            if temp==len(words)-1:
                output.append(i)
        return output