class Solution:
    def solution_1462_1(self, words: List[str]) -> int:
        dc=defaultdict(lambda:0)
        for a in words:
            dc[a]+=1
        count=0
        palindromswords=0
        inmiddle=0
        wds=set(words)
        for a in wds:
            if(a==a[::-1]):
                if(dc[a]%2==1):
                    inmiddle=1
                palindromswords+=(dc[a]//2)*2
            elif(dc[a[::-1]]>0):
                count+=(2*(min(dc[a],dc[a[::-1]])))
                dc[a]=0
        return (palindromswords+count+inmiddle)*2
        ``