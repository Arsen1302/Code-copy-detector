class Solution:
    def solution_873_4(self, s: str) -> List[str]:
        # s="TO BE OR NOT TO BE"
        l=s.split(' ')
        # print(l)
        maxlen=max(len(ele)for ele in l)
       # print(maxlen)
        m=[]
        for i in range(maxlen):
           str=''
           for word in l:
              if i>=len(word):
                 str+=' '
              else:
                 str+=word[i]
           m.append(str.rstrip())
        return m