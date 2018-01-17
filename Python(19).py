print "print even numbers between 1 to 100 using for loop"
for i in range(1,101):
    if (i %2==0):
        print i
        continue
print "By using For loop "    
def first():
    for i in range(1,101):
        if (i==50):
            break;
        elif (i==10 |i==20 |i==30|i==40|i==50):
            continue;
        if (i %2==0):
            print i
first()
print "by using While loop "
def second():
    value=1
    while(value<=100):
        if (value==90):
            break;
        elif (value==60 |value==70 |value==80|value==90):
            continue;
        if (value %2==0):
            print value
        value=value+1
second()    
    