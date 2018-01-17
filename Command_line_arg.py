import sys
for i in range(1,len(sys.argv)):
    print sys.argv[i]," "
if len(sys.argv) == 4 :
    f_num=sys.argv[1]
    s_num=sys.argv[2];
    t_num=sys.argv[3];
    if (f_num>s_num) and (f_num>t_num):
        print "first number is largest and the number is",f_num
    elif (s_num>f_num) and (s_num>t_num):
        print "second number is largest and the number is",s_num
    elif (t_num>f_num) and (t_num>s_num):
        print "third number is largest and the number is",t_num

