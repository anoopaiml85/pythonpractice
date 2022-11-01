
def bubblesort(num_sort):

    for j in range(len(num_sort)-1):
       # print(j)
        for i in range(len(num_sort)-1):
            
            if num_sort[i]>num_sort[i+1]:
                swap = num_sort[i]
                num_sort[i] =num_sort[i+1]
                num_sort[i+1]=swap
            #print(num_sort)
            else: 
                pass
    return (num_sort)

test=[5,4,3,2,1]
print(bubblesort (test))
