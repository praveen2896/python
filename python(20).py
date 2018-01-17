print "fibonacci numbers"
n=input("enter the value of n")
print n
def fib(n):
 a,b = 0,1
 print a
 print b
 for i in range(n-2):
  c=a+b
  a=b
  b=c
  print c
 
fib(n)  