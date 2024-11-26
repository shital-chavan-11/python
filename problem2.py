list1=[1,2,3,3,45,56]
list2=[]
list3=list(map(int,list1))
for i in list3:
    if i>10:
        list2.append('*')
    else:
        list2.append(i)
print(list2)