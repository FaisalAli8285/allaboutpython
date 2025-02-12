n=int(input ("Enter a number to print a table : "))
for i in range(1,11,1):{
    print(f"{n} * {i} = { n*i}")
}
print("While loop executed")
i=1
j=1
while(i<=10):
    print(f"{n} * {i} = { n*i}")
    i+=1
print("do While loop executed")
while True:
    print(f"{n} * {j} = { n*j}")
    j+=1
    if(j>10):
        break
   
