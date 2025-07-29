class Solution:
    def solution_521_2(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        res=[]
        i=0
        replace_map={i:(s,t) for i,s,t in zip( indices, sources, targets ) }
        
        while i<len(s):    
            
            if i in replace_map: #check all chars
               
                done,p,sw_ind=0,i,0   #done: to check if all word was seen in s, p:pointer of s, sw_ind:pointer for char is source word 
                source_word=replace_map[i][0]
                target=replace_map[i][1]
                while p<len(s) and sw_ind<len(source_word) and s[p]==source_word[sw_ind]: 
                    done+=1
                    p+=1
                    sw_ind+=1
                if done==len(source_word):  #so all source word was found, append target to res and advance i
                    res.append(target)
                    i=i+len(source_word)
                else:                      #so not all sourcce-word was found so append (i) to res and continue normally
                    res.append(s[i])
                    i+=1
            else:   #index not to be replaced append to res
                res.append(s[i])
                i+=1
                
                    
        return "".join(res)