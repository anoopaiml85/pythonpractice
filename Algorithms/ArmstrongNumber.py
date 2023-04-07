'''python Program to Check Armstrong Number
153 = 1*1*1 + 5*5*5 + 3*3*3'''



def armstrongnum(num):
    sum=0
    #print(num)
    #num=int(num)
    stage =num
    #print(stage)
    while stage >0:
        digit = stage % 10
        #print(digit)
        sum = sum + (digit**3)
        stage = stage//10
    if num ==sum:
        print('Number is Armstrong number')    
    else:
        print('Number is not Armstrong number')


armstrongnum(153)    