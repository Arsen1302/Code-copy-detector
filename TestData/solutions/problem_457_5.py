class Solution(object):
    def solution_457_5(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        h={}
        ## storing last occurance of each letter in hashtable
        for i in range(len(s)):
            h[s[i]]=i
        m=0
        a=[]
        ## 'a' stores the final result
        ## 'm' stores the largest value of letter's last occurance so far.
        ## if m equals i then it will be on sub array
        for i in range(len(s)):
            if h[s[i]]==i and m==i:              
                a.append(i-sum(a)+1)
                m=i+1
            else:
                if h[s[i]]>m:
                    m=h[s[i]]
        return a