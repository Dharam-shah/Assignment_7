def factorial(num):

     if num == 1:
         return 1
     else:
         return (num * factorial(num-1))
     return 1 if num == 1 else (num * factorial(num-1))
num = 5
print('Factorial of {} is {}'.format(num, factorial(num)))
dict = {factorial(num)}
print(dict)