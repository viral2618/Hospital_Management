# a=int(input("enter a number:"))
# if a%3==0 and a%5==0:
#     print("fuzzzzBuzzzzzzz")
# elif a%3==0:
#     print("Fuzzz")
# elif a%5==0 :
#     print("Buzzzz")
    
    
# a=float(input("enter your marks:"))
# b=float(input("Enter your marks:"))
# average=(a+b)/2
# print(average)

# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# print(a>=b)

# def viral(fun):
#     def saniya(*args):
#         print("helloo bhai")
#         res=fun(*args)
#         print(res)
#         print("Good byeee")
#     return saniya
# @viral
# def add(a,b):
#     return a+b
# a=add(10,20)
# print(a)

# String functionsss
# a="viral"
# b=a.endswith("la")   # it checks that it end with the give string or not
# print(b)

# a='viral'
# print(a.replace('viral','saniyaa'))

# a=input("enter your 1st name:")
# print(len(a))

# dollar='i have $500 $symbol is used madam'
# print(dollar.count('$'))


# #ternary operator
# food=input("enter here:")
# print("sweet") if food=='cake' or food=='jalabi' else print("not sweet")

# age=21
# vote=('Noo',"Yess") [age>=18 ]
# print(vote)

# #nesting
# age = 37
# if age >=18:
#     if age>=80:
#         print("cannot drive , your aged")
#     else:
#         print("can drive")
# else:
#     print('cannot drive,You are under age')
    
# user=input("enter your favorite movie:")
# user2=input("enter your favorite movie:")
# user3=input("enter your favorite movie:")
# movies=list()
# movies.append(user)
# movies.append(user2)
# movies.append(user3)
# print(movies)

# a=[1,2,3,4,5]
# copy_list=a.copy()
# copy_list.reverse()
# if a==copy_list:
#     print('palndrome')
# else:
#     print("not")


# a=("c","d","a","a","b","b","a")
# print(a.count('a'))

# a=["c","d","a","a","b","b","a"]
# a.sort()
# print(a)

# li=[1,2,3,4,5,6]
# li.append(20)
# print(li)
# li=[1,4,2,3,5,7,6,9,8]
# li.sort()
# print(li)

# li.insert(5,10)
# print(li)

    # Mutable
#String No	capitalize, center, count, endswith, find, index, split, strip
# List	Yes	append, insert, extend, remove, pop, clear, sort, reverse, copy, count, index
# Tuple	No	count, index


#dictionary
# info={
#     "name":'viral',
#     "age":21,
#     'cgpa':8.47,
#     "saniyaa":'girlfriend'
# }
# info["right now"]="Mca"         #to add new values
# print(info)
# print(info["saniyaa"])

# #nested dictionary
# nested={
#     'name':'Viral makwana',
#     'subject':{
#         'maths':88,
#         'eng':76,
#         'sci':77
#     }
# }
# a=nested.items()
# print(a)

# se={1,2,5,7,4,3,6}
# tup=(8,9,10)
# se.add(tup)
# print(se)
# set={1,2,3,}
# set2={3,4,5}
# set3=set.intersection(set2)
# print(set3)

# a=dict()
# student = input("Enter subject:")
# student2 = input("Enter subject:")
# student3 = input("Enter subject:")
# a['subject']=student
# a['subject2']=student2
# a['subject3']=student3
# print(a)

# se={9,'9.0'}  # you can't store 9,9.0 in the set u need to change there data type for that
# print(se)

# value={
#     ('float',9.0),
#        ('int',9)}
# print(value)

# i=1
# while i<=100:
#     print(i)
#     i+=1

# i=100
# while i>=1:
#     print(i)
#     i-=1

  
# n=int(input("ENter a number:"))  
# i=1
# while i<=10:
#     print(f'{n} x {i} = {n*i}' )
#     i+=1
    
    
# #traverse 
# nums=[1,4,9,16,25,36,49,64,81,100]
# heros=["ironman","thor","superman",'lokii']
# i=0
# while i<len(heros):
#     print(heros[i])
#     i+=1
# i=0
# while i<len(nums):
#     print(nums[i],end=" ")
#     i+=1
    
    
    
# #REFER FOR LEARNING WHILE LOOP 
# nums=(1,4,9,16,25,36,49,64,81,100,81,81)
# i=0
# x=81
# while i<len(nums):
#     if x == nums[i]:
#         print("we found the element we are searching for")
#         print(nums[i])
#         break
#     else:
#         print('finding..')
#     i+=1
# print(f'how many time it search in the list {i} times')


# i=0
# while i<=5:
#     if i == 3:
#         i+=1
#         continue              #acts as skip
#     print(i)
#     i+=1

# i=1
# while i<=10:
#     if i==3 or i==6:
#         i+=1
#         continue
#     print(i)
#     i+=1

# li=("viral","harry","abhishek","chetan","hrutik")
# for list in li:
#         print(list)
# else:
#     print("end")
    
# li=[1,4,9,16,25,36,49,64,81,100]
# for val in li:
#     print(val)
# li=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# for val in li:
#     if val==x:
#         print(f"found at {i} index")
#     i+=1
    
# for i in range(1,10):
#     print(i)    
    
# for i in range(2,20,2):
#     print(i)
# for i in range(1,100):
#     print(i)

# for i in range(100,0,-1):
#     print(i)
    
# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(f'{num} x {i} = {num*i}')
    
# for i in range(5):
#     pass                #it is null statement that does nothing .it is used as a placeholder for future code
# print("heyyy viral")


# Program to find sum                       #0+1=1
                                            #1+2=3
                                            #3+3=6
                                            #6+4=10
                                            #10+5=15
# n=int(input("enter a number:"))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)



# #FACTORIAL
# n=int(input("enter a number:"))
# i=1
# fact=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

# #FEBONACCI SERIES
# n=int(input("enter a number:"))
# a=0
# b=1
# print(a,b,end=" ")
# for _ in range(n):
#     c=a+b
#     print(c,end=" ")
#     a,b=b,c