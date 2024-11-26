str="helloworld1235"
alpha1=0
digit1=0
for i in str:
    if i.isalpha():
        alpha1+=1
    if i.isnumeric():
        digit1+=1
print("alphabetical",alpha1)
print("digits",digit1)