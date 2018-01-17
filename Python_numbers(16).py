def prime_number(number):
    print number
    answer="true"
    for i in range (2,number):
        temp=number%i
        if temp == 0:
            answer="false"
    if answer == "true":
        print number,"is a prime number"
    else :
        print number,"is not a prime number"
def prime(number):
    for i in range(2,number):
        answer="true"
        for j in range(2,i):
            temp=i%j
            if temp == 0:
                answer="false"
        if answer == "true":
            print i
value=input("Enter the number")
print value
prime_number(value)
print "Prime number upto ",value
prime(value)

            