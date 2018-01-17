list1=[]
No_of_elements=int(input("Enter the value of N "))
print No_of_elements,"\n"
for i in range (No_of_elements):
    num=input("enter the number ")
    print num,"\n"
    list1.append(num)
def maximum(list1):
    answer=max(list1)
    return answer
def minimum(list1):
    answer=min(list1)
    return answer

print "Maximum among the ",No_of_elements,"numbers is",maximum(list1) 
print "Minimum among the ",No_of_elements,"numbers is",minimum(list1) 