# sum of even number
'''
def even(n):
    sum=0
    for i in n:
      dig=int(i)
      if dig%2==0:
        sum+=dig
    print(sum) 
       
even("24536")

'''

# smallest prime digit in number  else there is no prime 

'''
n = "9837"
prime_digits = []

for i in n:
    dig = int(i)
    if dig > 1:  
        is_prime = True
        for j in range(2, int(dig ** 0.5) + 1):
            if dig % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_digits.append(dig)

if prime_digits:
    print(min(prime_digits))  
else:
    print("No prime digit found")

'''      


# armstrong number in a given range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for i in range(start, end + 1):
    temp = i
    l = len(str(i))  
    sum = 0
    while temp > 0:
        digit = temp % 10  
        sum += digit ** l  
        temp //= 10       

    if sum == i:
        print(i)






