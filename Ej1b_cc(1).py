Fib= []
for i,k in enumerate (range (16)): 
       if k <= 2:
          Fib.append (k)
       else:
          Fib.append (Fib[i - 2] + Fib[i - 1])
print (Fib)

