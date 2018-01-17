name=['praveen','kumar','sunil','harish','khan']
str=input("Enter the name you want to search ? ")
print str
if (str in name):
    print "yes the name is found in the list"
else :
    print "no the name is not found in the list"
def without():
    a=0
    for i in range(0,len(name)):
        if (str == name[i]):
            a=a+1
    if (a>0):
        print "yes the name is found in the list"
    else: 
        print "no the name is not found in the list"
without()   
def reverse():
    print "elements in reverse direction"
    for i in range(0,len(name)):
        print name[i][::-1]
reverse()