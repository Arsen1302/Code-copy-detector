class Solution:
    def solution_206_2(self, s: str, k: int) -> int:
        #sliding window and hashmap O(n) or Divide and conquer(O(n*n))
        n=len(s)
        ans=0     
        freq= Counter(s)
        max_nums=len(freq)
        for num in range(1,max_nums+1):
            counter=defaultdict(int)
            left=0
            for right in range(n):
                counter[s[right]]+=1 
                
                while len(counter)>num:
                    counter[s[left]]-=1
                    if counter[s[left]]==0:
                        del counter[s[left]]
                    left+=1
                for key in counter:
                    if counter[key]>=k :
                        flag=1
                    else:
                        flag=0
                        break
                if flag==1:
                    ans=max(ans,right-left+1)
        return ans