# Given arr , splitting the arr into halves.
#keep splitting till one element
#sort the individual arrays in pairs
#merge back two arrays at a time.

# arr=[3,1,4,5,6,8,9]

# 3,1,4,5    6,8,9

# 3,1 4,5   6,8  9

# 3 1 4 5 6 8 9 

# 1,3  4,5  6,8

# 1,3,4,5   6,8,9

def merge_sort(arr):
    if len(arr)>1:
        mid_index = len(arr)//2
        left_arr = arr[:mid_index]
        right_arr =arr[mid_index:]
        #print(left_arr,right_arr)
        merge_sort(left_arr)
        merge_sort(right_arr)
        i=0
        j=0
        k=0
        while i < len(left_arr) and j<len(right_arr):

            if left_arr[i] <= right_arr[j]:
               arr[k] = left_arr[i]
               i += 1
            else: 
               arr[k] = right_arr[j]
               j += 1
            k += 1
           
        while i<len(left_arr):
            print(i,k)
            arr[k] = left_arr[i]
            i += 1
            k += 1
        print(arr)     

        while j<len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        print(arr)   






arr = [8,5,3,1,2,5,7]
merge_sort(arr)
print(arr)
