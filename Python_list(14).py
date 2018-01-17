employee_id=[001,002,003,004,005,006,007,010,011,020,021]
employee_name=['praveen','sunil','gokul','mahesh','pravin','harish','rajesh','bala','muthu','kowshik','vignesh']
for i in range(0,len(employee_name)):
    print employee_name[i]
index=input("enter the index you want to print  ")
print index
print "employee_id","","employee_name"
print "   ",employee_id[index],"         ",employee_name[index]
list1= employee_name[3:9]
for i in range(0,len(list1)):
    print list1[i]
print "\n\n"    
list2= employee_name[2:]
for i in range(0,len(list2)):
    print list2[i]
repeat=input("enter the number of times you want to repeat")
print repeat
print employee_name*repeat
print employee_id*repeat
list3=employee_id+employee_name
print list3
for i in range(0,len(employee_id)):
    print employee_id[i]," ",employee_name[i]
    