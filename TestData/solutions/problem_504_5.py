class Solution:
    def solution_504_5(self, s: str) -> List[str]:
        #three choices add a ./_/nothing
        # we cannot add after a gap after last element is zero after a decimal
        #check decimal occured
        #if we are adding a gap we can make the decimal occured false
        #cannot add another 0 if decimal is not occured and last element is 0
        #cannot add more than one gap
        #check gap added
        
        #decimal occured
        #gap occured
        #if decimal occured we cannot add another decimal
        q=deque()
            
        q.append((s[1],False,False,0))
        a=set()
        s = s[1:-1]
        while q:
            st,gapocc,decimalocc,li = q.popleft()
            st2=st
            st = st.split(' ')[-1]
            if li==len(s)-1:
                ss = st2.split(' ')
                if len(ss)==2:
                    a.add('('+ss[0]+', '+ss[1]+')')
                continue
            ch = s[li+1]
            lch = st[-1]
            
            
            if li==len(s)-2:
                if decimalocc==False and gapocc:
                    if ch!='0':
                        q.append((st2+'.'+ch,gapocc,True,li+1))
                        
                    if float(st)!=0:
                        q.append((st2+ch,gapocc,decimalocc,li+1))
                    continue
                if decimalocc and gapocc:
                    if ch=='0':
                        continue
                    else:
                        q.append((st2+ch,gapocc,decimalocc,li+1))
                    continue
                if gapocc==False and decimalocc:
                    #if gap not made len of st>1
                    if lch!='0':                            
                        q.append((st2+' '+ch,True,decimalocc,li+1))
                        continue
                if not decimalocc and not gapocc:
                    q.append((st2+' '+ch,True,decimalocc,li+1))
                    continue
                    
            if decimalocc==False and gapocc:
                q.append((st2+'.'+ch,gapocc,True,li+1))
                if float(st)!=0:
                    q.append((st2+ch,gapocc,decimalocc,li+1))
            if decimalocc and gapocc==False:
                if lch!='0':
                    q.append((st2+' '+ch,True,False,li+1))
                q.append((st2+ch,gapocc,decimalocc,li+1))
            if decimalocc and gapocc:
                q.append((st2+ch,gapocc,decimalocc,li+1))
            if not decimalocc and not gapocc:
                if float(st)!=0:
                    q.append((st2+ch,gapocc,decimalocc,li+1))
                q.append((st2+' '+ch,True,False,li+1))
                q.append((st2+'.'+ch,gapocc,True,li+1))
                
        return a
        pass