print('hi')
print("""hi""")

# sep=, end=
print('2021', '05','04',sep='-' , end='\r') 
 
######################################
#              FORMAT
######################################
a = 'apple'
b= 'fruit'
print(f'{a} is {b}')
print('{} and {}'.format('you' , 'me'))
print('{0} and {1} and {0}'.format('you' , 'me'))
print('{a} and {b} and {a}'.format(a='you' ,b= 'me'))\

#%s:string, %d: decimal, %f: float
print("%s's favorite num is %d" %('John', 7))
print("Score: %2d, Price: %f" %(3412 , 45.2341))

# escape letter
print('\ttest\n')
print('\ttest\n')