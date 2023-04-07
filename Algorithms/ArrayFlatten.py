arr = [[1,2,3],[4,5,6],[7,8,[9,10],11]]
result =[]

for i in arr:
    for j in i:
        #print(type(j))
        if type(j)==list:
            #print(j)
            # for z in j:
            #result.append(*j)
            result = [*result,*j]
        else:
            result.append(j)
print(result)                    
