f_num=input("enter the first number\n")
print f_num
s_num=input("enter the second number\n")
print s_num
t_num=input("enter the third number\n")
print t_num
if (f_num>s_num) and (f_num>t_num):
    print "first number is largest and the number is",f_num
elif (s_num>f_num) and (s_num>t_num):
    print "second number is largest and the number is",s_num
elif (t_num>f_num) and (t_num>s_num):
    print "third number is largest and the number is",t_num
else :
    print "invalid data"
