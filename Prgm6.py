number= int(input("Enter a number:"))
count=0

for i in range(2,(number//2 +1)):
    if(number % i==0):
        count= 1
        break
if(count==0):
    print(number," is a prime number")
else:
    print(number," is not a prime number")