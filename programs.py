#sum of odd digits
 
'''

sum=0
a=6789
for i in str(a):
    digit=int(i)
    if digit%2!=0:
        # print(digit)
        sum=sum+digit
print(sum)

'''

# sum of digits of non prime number

'''
num=2958
sum=0
for i in str(num):
    dig=int(i)
    count=0
    if dig>1:
        for j in range (1,dig+1):
            if dig%j==0:
                count+=1
    if count!=2:
        print(dig)
        sum=sum+dig  
print(sum)

'''


#perfect number

'''
num=int(input("enter a number : "))   # 6,28
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num," is a perfect number") 
else:
    print(num,"is not a perfect number")

'''

# LCM

'''
a, b = 12, 18
gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
lcm = (a * b) // gcd
print("LCM is", lcm)
print("GCD is", gcd)

 '''



#greatest common divisor

'''
num1=24
num2=12
if num1<num2:
    small=num1
else:
    small=num2
while(True):
    if(num1%small==0 and num2%small==0):
        print(small)
        small-=1   

'''


                   






