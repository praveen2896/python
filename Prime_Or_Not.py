f_num=input("enter the first number\n")
print f_num
answer="true"
for i in range (2,f_num):
    temp=f_num%i
    if temp == 0:
        answer="false"
if answer == "true":
    print f_num,"is a prime number"
else :
    print f_num,"is not a prime number"
