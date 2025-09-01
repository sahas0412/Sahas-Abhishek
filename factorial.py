def factorial(x):
    i=1
    p=1
    for i in range(1,x+1): 
        p=p*i
        i+= 5
    print("answer",p)
x=int(input("enter number ="))
factorial(x)

print(list(range(10)))