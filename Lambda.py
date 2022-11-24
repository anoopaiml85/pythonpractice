#lambda arguments:expression
#Function can have any number of arguments but only one expression which is evaluated and resturned. 
#can be used whereever function objects are required
#syntactically restricted to a single expression. 

#example
str1= 'GeeksForGeeks'

rev_upper=lambda string:string.upper()[::-1]
print(rev_upper(str1))

#difference
#regular function
def cube(y):
    return y*y*y

print(cube(5))    
#lambda function
lambda_cube=lambda y: y*y*y
print(lambda_cube(5))

#find the max of two numbers

max2 = lambda a,b: a if (a>b) else b
print (max(1,2))


#Fizz bizz
