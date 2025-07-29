class Solution:
    def solution_1619_2(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        a=[]                        #to store answer of queries
        for q in queries: 
            ia=q[0]               #kth smallest value to be returned
            t=q[1]                #trim index
            temp=[]
            for n in nums:
                temp.append(int(n[-1*t:]))                  #using slicing just take last t elements
                
            temp1=[[temp[0],0]]                             #another list that will store sorted elements along with index
            for i in range(1,len(temp)):
                key=temp[i]
                j=len(temp1)-1
                while j>=0 and key<temp1[j][0]:        #using insertion sort, insert elements to new list also store index
                    j-=1
                temp1.insert(j+1,[key,i])
        
            a.append(temp1[ia-1][1])                     #append required index element 
            
        return a