# a=10
# b=20
# sum=a+b
# print(sum)

# # More number of lines 
# a=10
# b=20
# sum=a+b
# print(sum)

# def add(a,b):
#     sum=a+b
#     print(sum)
# add(10,20)
# add(50,90)

# def average(a,b,c):
#     ave=(a+b+c)/2
#     print(ave)
#     return ave
# average(10,20,30)
# # print(vii) 


# #default parameter
# def product(a=10,b=20):
#     return a*b
# print(product(20,40))


# li=[1,2,3,4,5,6,7,8,9]
# heroes=["ironman",'batman','thor']
# def len_of_list(list):
#     for i in list:
#         print(i,end=" ")

# len_of_list(li)
# len_of_list(heroes)

# n=int(input("enter a number:"))
# def factorial(n):
#     fact=1
#     i=1
#     while i<=n:
#         fact*=i
#         i+=1
#     return fact
# fa=factorial(n)
# print(fa)


# def INR_to_USD(amt):
#     return amt*86

# usd=INR_to_USD(5)
# print(f'INR:{usd}')

# n=int(input("enter a number:"))
# def even(n):
#     if n%2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")
# even(n)


def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
show(5)


def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return fact(n-1)*n
print("factorial is",fact(4))


#SUM OF NATURAL NUMBER:::::
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(5))


li=["abhishek","harry","Hrutik","chetan","viral"]
def find(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    find(list,idx+1)
find(li)

