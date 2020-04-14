lst=[]
print("Enter 5 names")
for i in range(0,5):
    a=str(input())
    lst.append(a)
print(lst)
print("Names with more than 5 letters are:")
for i in lst:
    if len(i)>=5:
        print(i,)