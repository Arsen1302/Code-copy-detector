class Solution:
    def solution_806_4(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        hashTable = {
            "lu": [],
            "uu": [],
            "ru": [],
            "rr": [],
            "rb": [],
            "bb": [],
            "lb": [],
            "ll": []
        }
        i,j = king
        for qi, qj in queens:
            #diagonal check
            if abs(qi-i) == abs(qj-j):
                # diagonal in upper half
                if qi < i:
                    #diagonal in upper left quater
                    if qj < j:
                        #checking for minimum distance from king
                        if hashTable['lu']:
                            if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['lu'])[0])+abs(j-(hashTable['lu'])[1])):
                                continue
                            else:
                                hashTable['lu'] = [qi,qj]
                        else:
                            hashTable['lu'] = [qi, qj]
                            continue
                    else:
                        if hashTable['ru']:
                            if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['ru'])[0])+abs(j-(hashTable['ru'])[1])):
                                continue
                            else:
                                hashTable['ru'] = [qi,qj]
                        else:
                            hashTable['ru'] = [qi, qj]
                            continue
                else:
                    if qj < j:
                        if  hashTable['lb']:
                            if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['lb'])[0])+abs(j-(hashTable['lb'])[1])):
                                continue
                            else:
                                hashTable['lb'] = [qi,qj]
                        else:
                            hashTable['lb'] = [qi, qj]
                            continue
                    else:
                        if  hashTable['rb']:
                            if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['rb'])[0])+abs(j-(hashTable['rb'])[1])):
                                continue
                            else:
                                hashTable['rb'] = [qi,qj]
                        else:
                            hashTable['rb'] = [qi, qj]
                            continue
                            
                    
            
            # horizontal check
            if qi == i:
                if qj < j:
                    if hashTable['ll']:
                        if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['ll'])[0])+abs(j-(hashTable['ll'])[1])):
                                continue
                        else:
                                hashTable['ll'] = [qi,qj]
                    else:
                        hashTable['ll'] = [qi, qj]
                        continue
                else:
                    if hashTable['rr']:
                        if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['rr'])[0])+abs(j-(hashTable['rr'])[1])):
                                continue
                        else:
                                hashTable['rr'] = [qi,qj]
                    else:
                        hashTable['rr'] = [qi, qj]
                        continue
            
            # vertical check
            if qj == j:
                if qi < i:
                    if  hashTable['uu']:
                        if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['uu'])[0])+abs(j-(hashTable['uu'])[1])):
                                continue
                        else:
                                hashTable['uu'] = [qi,qj]
                    else:
                        hashTable['uu'] = [qi, qj]
                        continue
                else:
                    if  hashTable['bb']:
                        if (abs(i-qi)+abs(j-qj)) > (abs(i-(hashTable['bb'])[0])+abs(j-(hashTable['bb'])[1])):
                                continue
                        else:
                                hashTable['bb'] = [qi,qj]
                    else:
                        hashTable['bb'] = [qi, qj]
                        continue
        ans= []
        for value in hashTable.values():
            if value:
                ans.append(value)
        return ans
		```