def fib(n):
    if n <= 2:
        return n
    else:
        return (fib(n - 2) + fib(n - 1))
print ([fib(i) for i in range(100)])
#a= [fib(i) for i in range(100)]
#print ("imprimo a: ",a)
'''
def imp(n):
    if n / 3 == 0:
        return n
    else:
        return 0
print ([imp(i) for i in a])
b= [imp(i) for i in a]
print (b)
sum (b)
print (sum(b))
'''





