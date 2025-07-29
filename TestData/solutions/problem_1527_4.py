class Solution:
    def solution_1527_4(self, queries: List[int], L: int) -> List[int]:
        l1=[]
        st=""
        
#         if we have 4 then break it 2 or we have 5 then also to 2

        if L%2==0:
            n=L//2-1
        else:
            n=L//2
            
            
            
#         starting from that length like if we have 2 then 10 find the power if we have 3 then 100 continue from that string 
        start=pow(10,n)
        for i in queries:
            print(start)
#             add that queries-1 in the start 
            ans=str(start+i-1)
            
#         reverse that string 
            rev=ans[::-1]
    
#           if the length is the even simple ad the reverse string    
            if L%2==0:
                st=ans+rev
            
#             other wise add from the 1 index like k=3 string 10 then we have to just add the 1 to make the final string 101
            else:
                st=ans+rev[1:]
            
#           if the string length matches the given length then add in the result otherwise -1
            if len(st)==L:
                l1.append(st)
            else:
                l1.append(-1)
            # print(st,l1)
        return l1