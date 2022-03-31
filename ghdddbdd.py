# h, m = input().split()
# h = int(h)
# m = int(m)
# timer = int(input())
# m += timer
# h += m // 60
# m %= 60
# if h >= 24:
#     h %= 24
# print(h , m)
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# if a == b and b == c:
#     print(10000+a * 1000)
# elif a == b and b != c:
#     print(1000 + a * 100)
# elif a != b and b == c:
#     print(1000 + b * 100)
# elif a == c and b != c:
#     print(1000 + c * 100)
# else:
#     if a >b and a>c:
#         print(a * 100)
#     elif b>a and b>c:
#         print(b * 100)
#     else:
# #         print(c*100)
# n = int(input())
# a = input().split()
#
# min = int(a[0])
# max = int(a[0])
#
# for i in a:
#     if min >int(i):
#         min = int(i)
#     if max < int(i):
#         max = int(i)
# print(min,max)
# a = []
# for i in range(9):
#     a.append(int(input()))
#
#
# max = int(a[0])
# for i in a:
#     if max < i:
#         max = int(i)
#
# b = a.index(max)
# print(max)
# print(b+1)
# a= int(input())
# b= int(input())
# c= int(input())
# d = str(a * b * c)
#
# for i in range(10):
#     print(d.count(str(i))
# b = []
# for i in range(10):
#     a = int(input()) % 42
#     if a not in b:
#         b.append(a)
n = int(input())
a = input().split()
m = 0
for i in a:
    if m < int(i):
        m = int(i)
q = []
for i in a:
    q.append(int(i)/m*100)
s = 0
for i in q:
    s += i
print(s/n)