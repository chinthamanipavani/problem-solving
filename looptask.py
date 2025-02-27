#write aprogram to calculate factorial of a given number

n=int(input("enter a number : "))
fact=1
if n==0:
    print(fact)
elif n<0:
    print("factorial does not exists ")
else:
    while n>0:
        fact=fact*n
        n=n-1
        #print(fact)
    print(fact)         
        

     
#  Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.


n1=int(input("enter a value of n1 : "))
for i in range(1,n1+1):
  if i%3==0 and i%5==0:
      print(i)



#to print tables

n2=int (input("enter n2 value : "))
n3=int(input("enter n3 value : "))
for i in range (1,n2+1):
     for j in range(1,n3+1):
          result=i*j
          print(result)
