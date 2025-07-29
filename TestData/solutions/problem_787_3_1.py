class Solution:
    def solution_787_3_1(self, arr: List[int]) -> int:
        def solution_787_3_2():
		
			res=-sys.maxsize
            cur_max,max_so_far=arr[0],arr[0] 
            fw[0]=cur_max 

            for i in range(1,n): 
                cur_max=max(arr[i], cur_max + arr[i]) 
                max_so_far=max(max_so_far, cur_max) 
                fw[i] = cur_max 
				res=max(res,max_so_far)
				
            cur_max=max_so_far=bw[n-1]=arr[n-1] 
            
            i=n-2
            while i>=0: 
                cur_max=max(arr[i],cur_max+arr[i]) 
                max_so_far=max(max_so_far,cur_max) 
                bw[i]=cur_max 
				res=max(res,max_so_far)

                i-=1
          
            i=0
            while(i<n):
                x=max(i-1,0)
                y=min(i+1,n-1)
                if x!=y:
                    res=max(res,fw[x]+bw[y])
                i+=1
            
            return res

        n = len(arr) 
        fw = [0 for k in range(n)] 
        bw = [0 for k in range(n)] 
        
        return solution_787_3_2()