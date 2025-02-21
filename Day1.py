#gretest of three numbers

'''
num1 = int(input("enter num1 : "))
num2 = int(input("enter a num2 : "))
num3 = int(input("enter num3 : "))
if num1==num2 or num1== num3 or num2==num3: 
       print("don't repeat the number")
else:
       if num1>num2 and num1>num3 :
        print( num1,"is greater")
       elif num2>num1 and num2>num3:
        print(num2,"is greater ")  
       elif num3>num1 and num3>num1:
        print(num3," is greater ") 

'''   
   
#student marks

'''
marks=int(input("enter marks"))    
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B ") 
elif marks>=70 and marks<=79 :
    print("Grade C") 
elif marks<70:
    print("fail ")         
else:
    print("marks should be in 1-100")

'''

#triangle

'''
side1=int(input("enter side1 : "))
side2=int(input("enter side2 value: "))
side3= int(input("enter side3 value : "))
if side1>0 and side2>0 and side3>0:
    if side1+side2==side3 or side1+side3==side3 or side2+side3==side1:
        print("it is not a triangle")
    else:
        print("it is a triangle ")

'''  

#vowel ,consonents and neighter

'''
char=str(input("enter a character : ").lower())
if char in (['a','e','i','o','u']):
    print("vowel")
elif char in (['b','d','f','g','h','j','k','l','m','n','p' ,'q','r','s','t','v','w','x','y','z']):
    print("consonents")
else:
    print("neighter")   
    
'''

#leap year

year=int(input("enter a year : "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"leap year")
else:
    print(year,"not a leap year : ")    



# side1+side=side3
# it isnot a triangle
