a=eval(input("enter the list"))
b=eval(input("enter the string u have to find:"))
c=[]
for i in a:
    if i.startswith(a)==True:
        c.append(i)
print(c)
