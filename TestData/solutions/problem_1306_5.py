class Solution:
    def solution_1306_5(self, grid: List[List[int]], k: int) -> List[List[int]]:

        #element ordered in row manner, grouped by layer
        rows=len(grid)
        cols=len(grid[0])
        layers=min(rows//2,cols//2)
        sliced_grid=[[] for _ in range(layers)]
        for i in range(rows):
            layers_in_this_row=min(i+1,rows-i)
            for j in range(cols):
                sliced_grid[min(min(j,cols-j-1),layers_in_this_row-1)].append(grid[i][j])
        print(sliced_grid)

        #reshape layer, element ordered in clockwise manner
        reshaped=[[0 for __ in range(len(slice)) ] for slice in sliced_grid]
        for layer,layer_item in enumerate(sliced_grid):
            back_trace_id=-1
            back=True
            top_row_element_count=cols-layer*2
            for idx,item in enumerate(layer_item):
                if idx<top_row_element_count:
                    reshaped[layer][idx]=item
                elif idx<len(layer_item)-top_row_element_count and back:
                    reshaped[layer][back_trace_id]=item
                    back=not back
                    back_trace_id-=1
                elif idx<len(layer_item)-top_row_element_count and not back:                    
                    reshaped[layer][idx+back_trace_id+1]=item
                    back=not back
                else:
                    reshaped[layer][back_trace_id]=item
                    back_trace_id-=1
        print(reshaped)

        #reconstruct to traditional row format, rotate by offset
        offset=k
        reconstruct=[[0 for _ in range(cols)] for _ in range(rows)]
        offset_count=[[0,len(reshaped[layer])-1,True] for layer in range(layers)]
        for i in range(rows):
            layers_in_this_row=min(i+1,rows-i)
            for j in range(cols):
                layer=min(min(j,cols-j-1),layers_in_this_row-1)
                top_row_element_count=cols-layer*2
                if offset_count[layer][0]<top_row_element_count:
                    reconstruct[i][j]=reshaped[layer][(offset+offset_count[layer][0])%len(reshaped[layer])]
                    offset_count[layer][0]+=1
                elif offset_count[layer][0]<len(reshaped[layer])-top_row_element_count and offset_count[layer][2]:
                    reconstruct[i][j]=reshaped[layer][(offset+offset_count[layer][1])%len(reshaped[layer])]
                    offset_count[layer][0]+=1
                    offset_count[layer][1]-=1
                    offset_count[layer][2] = not offset_count[layer][2]
                elif offset_count[layer][0]<len(reshaped[layer])-top_row_element_count and not offset_count[layer][2]:   
                    reconstruct[i][j]=reshaped[layer][(offset+offset_count[layer][0]-(len(reshaped[layer])-offset_count[layer][1]-1))%len(reshaped[layer])]
                    offset_count[layer][0]+=1
                    offset_count[layer][2] = not offset_count[layer][2]
                else:             
                    reconstruct[i][j]=reshaped[layer][(offset+offset_count[layer][1])%len(reshaped[layer])]
                    offset_count[layer][1]-=1

        print(reconstruct)
        return reconstruct