my_num = 2836
rev_num = 0
while my_num>0:
    rem = my_num%10
    my_num=my_num//10
    rev_num = (rev_num*10)+rem
    
print(rev_num)
   