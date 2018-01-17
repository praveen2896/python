numbers=[]
for i in range(0,10):
    numbers.append(input("enter the values \n"))
    print numbers[i]
print numbers
sum=0.0
for i in range(0,len(numbers)):
   sum+=numbers[i]
print sum
average=sum/len(numbers)
print average
greater=0
equall=0
for i in range(0,len(numbers)):
    if (numbers[i] == average):
        equall+=1
    elif (numbers[i] >average):    
        greater+=1
print "no of elements greater than average ",greater
print "no of elemwnts equal to avearage ",equall

