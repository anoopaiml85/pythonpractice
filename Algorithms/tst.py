lst = [1,2,3,4,5]

lst2= []

for i in range(len(lst)):
    lst2.append(lst[i]+2)
print(lst2)

lst3 = [x+2 for x in lst2]
print(lst3)