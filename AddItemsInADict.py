test_dict = {'a':100,'b':200,'c':300}
# print(test_dict['a'])
# print(test_dict.items())
# print(test_dict.values())
# print(test_dict.keys())
totalsum=0
for val in test_dict.values():
    totalsum = totalsum + val
#print (totalsum)    

for name,val in test_dict.items():
  print(name,val)