class Solution:
    def solution_1717_5(self, message: str, limit: int) -> List[str]:
        l=len(message)
        if limit<=5:
            return []
        min_size=None
        min_ct=0
        for ct in range(1, min(((limit-4)>>1)+1, 6)):
            total=0
            for i in range(1, ct):
                total+=(9*10**(i-1))*(limit-i-ct-3)
            left=l-total
            if left<0:
                continue
            left_size=(left-1)//(limit-2*ct-3)+1
            if left_size>9*10**(ct-1):
                continue
            total_size=left_size+10**(ct-1)-1
            if (min_size==None or total_size<min_size):
                min_size=total_size
                min_ct=ct
        if min_size==None:
            return []
        else:
            str_total_size=str(min_size)
            ans=[]
            curs=0
            for i in range(min_size-1):
                new_curs=curs+limit-(int(log10(i+1))+1)-min_ct-3
                # print(limit, (int(log10(i+1))+1), min_ct)
                ans.append(message[curs:new_curs]+'<'+str(i+1)+'/'+str_total_size+'>')
                curs=new_curs
            ans.append(message[curs:]+'<'+str_total_size+'/'+str_total_size+'>')
            return ans