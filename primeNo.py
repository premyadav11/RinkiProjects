num=int(input("Enter a number: "))
i=2
while(i<num):
    if(num % i == 0):
        print("Number {} is not prime number".format(num))
        break
    i+=1
    if(i == num):
        print("Number {} is prime number".format(num))

