mycurrency =346789

bills=[2000,500,200,100,50,20,10,5,2,1]

for i in bills:
    count = mycurrency//i
    mycurrency=mycurrency%i
    print(f'Total number of {i} bills:{count}')

# note_dict= {'2000':0 ,'500':0,'200':0,'100':0,'50':0,'20':0,'10':0,'5':0,'2':0,'1':0}
# for key,val in note_dict.items():
#     key =int(key)
#     if mycurrency >= key:
#         note_dict[key]=mycurrency//key
#         mycurrency=mycurrency%key
#         print(note_dict)


