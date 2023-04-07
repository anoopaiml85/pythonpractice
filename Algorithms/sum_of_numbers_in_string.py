# "10Abcd30 BSADCD20GHI"
# 10+20+30 = 60

str='10Abcd30 BSADCD20GHI'
num=0
sum=0

for i in str:
    
    if i.isdigit():
        num =num*10 + int(i)

    else:
        sum=sum+num
        num=0
print(sum)        