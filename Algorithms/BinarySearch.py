#List of numbers
#sort them first
#find the length of the array
#query the middle element
#check if the middle element is greater or less than the search eliment
#move left or right depending on it the element is less or greater.

def binarysearch(my_list,search_element):
    # sortedlist = bubblesort(my_list)
    # print (sortedlist)
    MaxLength = len(my_list)
    #print(MaxLength)
    IndexIntialPosition = 0
    IndexLastPosition = MaxLength - 1
    #Taking the mid-value of index to start the search

    while IndexIntialPosition <=IndexLastPosition:
        MidIndex = IndexLastPosition+IndexIntialPosition//2
        #print(MidIndex)
    #Check if midIndex position is equal to the search element
        if my_list[MidIndex] < search_element:
            #print('inside less than')
            IndexIntialPosition = MidIndex +1 
        elif my_list[MidIndex] > search_element:
            IndexLastPosition = MidIndex-1
            #print('inside greater than')
        else:
            return MidIndex    
    return -1      

output=binarysearch([1,2,3,4,5,6,7,8,9],3)
print(f'Element is found at the index {output}')