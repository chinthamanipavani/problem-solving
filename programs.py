

#1.Create a function that takes two numbers as arguments and returns their sum.

'''
def sum(n1,n2):
    return n1+n2
print(sum(5,6))
'''
#2. Write a function that takes an integer minutes and converts it to seconds.


'''
def convert(min):
    sec=min*60
    print(sec)
convert(3)   
''' 
#3 .Create a function that takes a number as an argument, increments the number by +1 and returns the result.

'''
def num(n):
    return n+1
print(num(5))
'''
#4.Create a function that takes the age in years and returns the age in days. 

'''
def age(a):
    res=a*365
    print(res)
age(5)
'''   
#5. sbi Create a function that takes voltage and current and returns the calculated power.

'''
def sbi(voltage,current):
    power=voltage*current
    print(power)
sbi(200,20)

'''
#6. Write a function that returns the string "something" joined with a space " " and the given argument a.

'''
def string(input):
    return " "+input
print(string("something"))
'''
#7. Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.

'''
def num(a,b):
    if a==10 or b==10 or a+b==10:
        return True
print(num(3,7)) 
'''  
#8. Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.

'''
def string(str1,str2):
    if(len(str1)==len(str2)) :
        return True
    return False
print(string("hello","goods"))
'''


#9. 
'''

def greet(name):
    return "hello " + name +"! nice to meet you"
print(greet("pavani"))
'''

#10 . Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555)

'''
list1=[6,4,6,9]
for i in list1:
    # print(i)
    res=(str(i))
    print(res ,end="")

print(type(i))
def array(a):
    res=str(a)
    return res
print([0,1,2,3,4,5,6,7,8,9])
'''

# 11. Create a function that returns an array of strings sorted by length in ascending order.
# Example:
# sortByLength(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]

'''
list2=["a","aaaaa","aaa","aa","aaaa"]
n=len(list2)
for i in range(n):
    for j in range(0,n-i-1):
        if len(list2[j])>len(list2[j+1]):
            temp=list2[j]
            list2[j]=list2[j+1]
            list2[j+1]=temp
print(list2[-1])

'''     


#12   
#Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.
# Example:
# findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]


'''
list1=[
    [5,6,7],
    [9,1,88],
    [99,0,77]
]
r=[]
for i in list1:
    largest=i[0]
    for j in i:
        if j>largest:
          largest=j        
    r.append(largest)
print(r) 

'''

#13.second largest element in an list
'''
l1=[55,73,61,11,99,56,98]
largest=slrgest=float('-inf')#-n
for i in l1:#55,73,61,11
    if i>largest:#55>-n,73>55,61>73,11>73
        slargest=largest#-n,55
        largest=i#55,73
    elif i>slargest and i!=largest:#61>55&61!=73,11>61
        slargest= i   

print(slargest)

'''
#14.remove duplicates in list and biggest number in that list

'''
list1=[11,90,10,11,23,90,11]
a=[]

for i in list1:
    if i not in a:
        a.append(i)
        k=a[0]
        for j in a:
            # if j>k:
            #     k=j
            if j<k:
                k=j
print(a)  
print(k) 

'''
#15
#[2,2,2,2,1,1,1,4,4,4,4,7]==>o/p=7
'''
list1=[2,2,2,2,1,1,1,4,5,3,4,4,4,2,2,7]
for i in list1:
    if list1.count(i)==1:   #count how many times iterate in the list
        print(i)
        # break   #5'
'''
#16..Create a function that takes a string and returns the number (count) of vowels contained within it. ex:- ("a", "banana"))  # Output: 3,(b,"banana")  # Output: 1  ,("c","banana")  # Output: 0

'''
string1="a"
string2="banana"
count=0
n=[]
for i in string2:
   if i==string1:
      count+=1
print(count) '
'''

# 17..Create a function that takes a string and returns the number (count) of vowels contained within it.
#way-1
'''
string1="GOOD morning"
for i in string1:
    # if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
    #     print(i,end="")
    # L=i.lower()
    # print(L,end="")

'''
#way-2
'''
string2="GOOD morning"
for i in string2:    
    if i.lower() in "aeiou" :  #in  and ==  both are different 
     print(i)

'''

#18 ...Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
# Example:
# reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"
'''
def reverseCase(string):
    string=string.swapcase()
    return string
print(reverseCase("Happy Birthday"))

'''


#19..Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.		
# 			Input:      n=5
# 			Output:   2 4 6 8 10

# 			Explanation:  Loop start with 1 go till 5 bcoz n=5
# 					1 x 2 =2, 2 x 2=4, 3 x 2=6 …..etc 

'''
l=int(input("enter the l :"))
def num(n):
 for i in range(1,n+1):
    m=i*l
    print(m,end=" ")
num(5)

''' 

#20... Create Function that will take one parameter and return type of the data.
			
			# Input:       500
			# Output:     Integer

			# Input:     Coding
			# Output:    String
'''
def name(s):
    print(type(s))
name("pavani")

# n=9898
# print(type(n)) 

'''  

#   21. Program to find greatest of three numbers(using ternary operator).		Input:  4 8 2   Output: 8 is greatest
'''
def num(n,n2,n3):
    result=str(n)+"big" if n>n2 and n>n3 else  str(n2)+ "is big" if n2>n and n2>n3 else str(n3) + "is big"
    print(result)
num(6,12,3) 

'''   

# 22 .Program to find factorial of number.
'''
def factorial(n):    
    fact=1
    if n>1:
        for i in range(1,n+1):
            fact=fact*i	
    print(fact)	
factorial(5)    

'''
#23.Program to arrange numbers in ascending order   Input: [2,3,1,5,4]     Output: [1,2,3,4,5]
'''
list1 = [1, 4, 99, 1, 2, 77]
n = len(list1)
for i in range(n - 1):        
    for j in range(n - 1 - i):  
        if list1[j] > list1[j + 1]:  # Swap if the left element is greater
            temp=list1[j]              
            list1[j]=list1[j+1]       
            list1[j+1]=temp          

print(list1)

'''

#24. Print Patter using loop.

			# 1
			# 1 2
			# 1 2 3
			# 1 2 3 4
  			# 1 2 3 4 5
              
'''
n=5
for i in range(n+1):
  for j in range(1 ,i+1):
    print(j,end=" ")
  print()

'''  

#25..Program to Calculate the Power of a Number(using loop only).  Input: n=5, p=3   Output: 5 ^ 3 = 125     Explanation: 5 x 5 x 5 = 125

'''
n=5
p=3
r=1
for i in range(3):
    r=r*n  #5 ,25,125
print(r)

'''
#26.prime number or not
'''
def prime(n):
    if n<1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
if prime(9)==True:
    print("prime") 

'''      
#27  lcm of 2 numbers 
''''

n1=6
n2=4
if n1>n2:
    greater=n1
else:
    greater=n2
while True:
    if greater%n1==0 and greater%n2==0:
       print(greater)
       break
    greater+=1

'''
#28. Program to Display Characters from A to Z Using Loop with count.            Output: A1 B2 C3 D4 E5 F6 ……. Z26 

'''
for i in range(0,26):
    letter=chr(65+i) 
    print(f"{letter} {i+1}", end=" ")

'''

#29. Program to find a missing number  Input:  n=5(length of array), arr= [5,3,1,4]  Output: 2 is missin   Using loop only(you can not use predefined function)

'''
n=7
a=[1,2,4,6,5,7]
sum1=0
sum2=0
for i in range(1,n+1):
    sum1=sum1+i#1+2+3+4+5+6+7==>28
print(sum1)
for j in a:
    sum2=sum2+j
print(sum2)#1+2+4+6+5+7==>25
missing=sum1-sum2 
print(missing)  

'''
#30. Program to count vowels and consonants in a given String.  Input: i am ram      Output: 3 vowels 3 consonants.
'''
string="good morning"
count1=0
count2=0
for i in string:
    if i in['a','e','i','o','u']:
        count1+=1
    elif i in ['b','c','d','f','g','h','j','k','l','m','n','n','p','q','r','s','t','v','w','x','y','z']:
        count2+=1
print(count1)
print(count2)

'''
#31. program to insert  the elements of an array for specific index.Input: [1,2,3,4,5,7,8,9,10] , index=5    Output: [1,2,3,4,5,6,7,8,9,10]
'''
a=[1,2,3,4,5,6,8]
index=6
element=7
new=[]
for i in range(0,len(a)+1):
    if i<index:
        new.append(a[i])
    elif i==index:
        new.append(element)     
    else:
        new.append(a[i-1])
print(new)    

''' 

#32. Reverse a number using while Loop    Input: 123    Output: 321
'''
n=123
rev=0
while n>0:
    l=n%10   #3
    rev=rev*10+l
    n=n//10
print(rev) 

'''  
#33. Count occurrence of number:   Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7      Output: 7 present 2 times.

'''
a=[1,6,3,1,5,9,7,2,1,9,3,7,8,9,10]
count=0
num=int(input("enter a number"))
for i in a:
    if i==num:
        count+=1
print(f"{num} present {count} times")        

'''

