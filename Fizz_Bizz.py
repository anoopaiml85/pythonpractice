total_number = 100

for i in range(0,100):
    if i%3==0 | i%5==0:
        print('FIZZBIZZ')  
    elif i%3==0:
       print('Fizz')
    elif i%5==0:
       print('Bizz')  
    
    else:
        print(i)    