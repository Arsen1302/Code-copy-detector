class Solution:
    def solution_329_1(self, n: int) -> int:
        m=list(str(n))                       ## n = 257761
        l = len(m)                           ## l = 6
        d = {}
        res = str(n)
        
        ## reading character backwards: 1->6->7->7->5 break
        for i,c in enumerate(m[::-1]): 
            if not d:
                d[c]=1                       ## d = {'1':1}
            else:
                if all(c >= x for x in d):
                    d[c]=d.get(c,0)+1        ## d = {'1':1,'6':1,'7':2} 
                else:
                    d[c]=d.get(c,0)+1        ## d = {'1':1,'5':1,'6':1,'7':2}
                    res = ''.join(m[:l-1-i])        ## res = '2'
                    stock = sorted(list(d.keys()))  ## stock = ['1','5','6','7']
                    cplus = stock[stock.index(c)+1] ## cplus = '6' just > '5'
                    res += cplus                    ## res = '26'
                    d[cplus] -= 1                   ## d = {'1':1,'5':1,'6':0,'7':2}
                    res += ''.join([x * d[x] for x in stock]) 
					                                ## res = '26' + '1577'
                    break
        
        return int(res) if n < int(res) < (2**31-1) else -1