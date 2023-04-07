# test = 'barbados'
# testdict= {}
# #loop throurgh the string and update count in dict.
# for i in test:
#     count = 0
#     for j in test:
#         if i==j:
#             count =count+1
#     testdict[i] = count 
# print(testdict)     
# #print (testdict.values()) 
# #print (testdict.keys()) 
# print(testdict.items())
# for key,val in testdict.items():
#     if val ==1:
#         print (key) 
       
#         break
def first_np_character(STR):
    hash_dict = {}
    for x in STR:
        if hash_dict.get(x):
            hash_dict[x] += 1
        else:
            hash_dict[x] = 1
    
    for i in range(len(STR)):
        if hash_dict.get(STR[i]) == 1:
            return i

    return -1 


print(first_np_character("barbados"))

# Declare an Array.
# [3,2,5,8,6]
# takes each element and compares first two positions.
# if first is greater than second swap positions.
