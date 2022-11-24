#def calc_factorial(num)
# def test_fact(num):
#     fact =1
#     for i in range(1,num+1):
#     #print(i)
#         fact = fact*i
#     return(fact)

# print(test_fact(6))

# recursion
#example: factorial of 6  = 6*5*4*3*2*1
#1 - 6*5!
#2 - 5*4!
#3 - 4*3!
#4 - 3*2!
#5 - 2*1!
#6 - 1

def factorial(n):
    if n==1:
        return 1 
    return n*factorial(n-1)

print(factorial(7))