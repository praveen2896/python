def num ():
    numbers=[]
    for i in range(0,4):
        numbers.append(input("enter the values \n"))
        print numbers[i]
    if (numbers[0]>numbers[1]) and (numbers[0]>numbers[2]) and (numbers[0]>numbers[3]):
        print "first number is largest and the number is",numbers[0]
    elif (numbers[1]>numbers[0]) and (numbers[1]>numbers[2]) and (numbers[1]>numbers[3]):
        print "second number is largest and the number is",numbers[1]
    elif (numbers[2]>numbers[0]) and (numbers[2]>numbers[1]) and (numbers[2]>numbers[3]):
        print "third number is largest and the number is",numbers[2]
    elif (numbers[3]>numbers[0]) and (numbers[3]>numbers[1]) and (numbers[3]>numbers[2]):
        print "fourth number is largest and the number is",numbers[3]
    else :
        print "invalid data"

    return numbers 
def solution():
    numbers=num()
    print numbers;
    a=input("enter the fifith number to calculate")
    print a
    numbers.append(a)
    if (numbers[0]>numbers[1]) and (numbers[0]>numbers[2]) and (numbers[0]>numbers[3]) and (numbers[0]>numbers[4]):
        print "first number is largest and the number is",numbers[0]
    elif (numbers[1]>numbers[0]) and (numbers[1]>numbers[2]) and (numbers[1]>numbers[3]) and (numbers[1]>numbers[4]):
        print "second number is largest and the number is",numbers[1]
    elif (numbers[2]>numbers[0]) and (numbers[2]>numbers[1]) and (numbers[2]>numbers[3]) and (numbers[2]>numbers[4]):
        print "third number is largest and the number is",numbers[2]
    elif (numbers[3]>numbers[0]) and (numbers[3]>numbers[1]) and (numbers[3]>numbers[2]) and (numbers[3]>numbers[4]):
        print "fourth number is largest and the number is",numbers[3]
    elif (numbers[4]>numbers[0]) and (numbers[4]>numbers[1]) and (numbers[4]>numbers[2]) and (numbers[4]>numbers[3]):
        print "fifth number is largest and the number is",numbers[4]
    else :
        print "invalid data"
    return 
solution()