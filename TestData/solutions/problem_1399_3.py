class Solution:
    def solution_1399_3(self, sentence: str) -> int:
        a = list(sentence.split())
        res=0
        punc = ['!','.',',']
        
        for s in a:
            if s!="":
                num=0
                for i in range(0,10):
                    num+=s.count(str(i))
                if num==0:
                    k=s.count('-')
                    if k==0 or (k==1 and s.index('-')!=0 and s.index('-')!=len(s)-1):
                        num=0
                        for i in punc:
                            num+=s.count(i)
                        if num==0 or (num==1 and s[-1] in punc and (len(s)==1 or s[-2]!='-')):
                            res+=1
        return res