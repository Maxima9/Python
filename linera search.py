list=[4,8,9,3,6]
n=9
pos=0
def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
    return False

if search(list,n):
    print("Found at",pos+1)
else:
    print("Not Found")