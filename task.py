
# sum of a digits 


def digit(n2):
    if n2<10:
        return n2
    return n2%10+digit(n2//10)
new=digit(289)
print(new)



#reverse a list


list1=[3,2,4,5,8]
empty=[]
l=len(list1)-1
def rev(l):
   if l<0:
      return 
   empty.append(list1[l])
   return rev(l-1)
rev(len(list1)-1)
print(empty)

   
   
