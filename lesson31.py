#Write a program to check if the number entered by the user is an Armstrong number or not?

c=int(input("enter the value"))
sum=0
tem=c
while tem > 0:
    digit=tem%10
    sum += digit**3
    tem //= 10

if c==sum:
    print("amstrong number")

else:
    print("it is not an amstrong number")        