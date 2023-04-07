#in a list find a number if it exists.
#Compare with the first element if not equal move on to the next. 

lst = [4,2,6,7,9,4,6,8,1,12,13,17]
find= 13
i=0
while i<len(lst):
    if lst[i]==find:
        print( 'found the number at index: ',i)
        break
    else:
        i=i+1   
print("not found")
