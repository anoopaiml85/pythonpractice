def perm(lst,f=0):
    if f>=len(lst):
        print(lst)
        return
    for s in range(f,len(lst)):
        lst[f],lst[s]=lst[s],lst[f]
        #print(f'intial swap{lst}')
        perm(lst,f+1)
        lst[f],lst[s]=lst[s],lst[f]
        #print(f'reset{lst}')        


perm([1,2,3])