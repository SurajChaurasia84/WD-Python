a=[1,2,3,"hello",3.4,"my",5.5,4.8]
b=[]
for i in a:
    if(type(i)==int):
        b.append(i)     
a=b
print(a)