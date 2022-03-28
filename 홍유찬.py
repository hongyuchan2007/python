# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for i in range(len(data)):
#     for x in range(len(data)+1):
#         print(data[i][x]+data[i][x]*0.00014)
#     print('----------')
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for i in range(len(data)):
#     for x in range(len(data)+1):
#         result.append(data[i][x]+data[i][x]*0.00014)
# print(result)
# result = []
# for i in range(len(data)):
#     a = []
#     for x in range(len(data)+1):
#         a.append(data[i][x]+data[i][x]*0.00014)
#     result.append(a)
# print(result)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(len(ohlc)-1):
#     print(ohlc[i+1][3])
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(len(ohlc)-1):
#     if ohlc[i+1][3] > 150:
#         print(ohlc[i+1][3])
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(len(ohlc)-1):
#     if ohlc[i + 1][3] >= ohlc[i + 1][0] :
#         print(ohlc[i + 1][3])
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for i in range(len(ohlc)-1):
#     volatility.append(ohlc[i+1][1]-ohlc[i+1][2])
# print(volatility)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(1,len(ohlc)):
#     if ohlc[i][0] < ohlc[i][3]:
#         print(ohlc[i][1]-ohlc[i][2])
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# a = 0
# for i in range(1,len(ohlc)):
#     a +=ohlc[i][3]-ohlc[i][0]
# print(a)
#except= 예외
# while True:
#     a,b = input().split(',')
#     print(int(a)+ int(b))
#     if a == '0' and b == '0':
#         break
# T = int(input())
# for i in range(T):
#     a,b = input().split()
#     print("case #%d :%d + %d = %d"%(i+1, int(a), int(b),int(a)+int(b)))
# a, b = input().split( )
# if int(a) > int(b):
#     print('>')
# elif int(a) < int(b):
#     print('<')
# else:
#     print("==")
# a = int(input())
# if a % 4 == 0 and a % 100 !=0 or a % 400 == 0:
#     print(1)
# else:
#     print(0)
# x = int(input())
# y = int(input())
# if  x > 0 and y>0:
#     print(1)
# elif x < 0 and y>0:
#     print(2)
# elif x < 0 and y<0:
#     print(3)
# else:
#     print(4)
H, M = input().split()
H = int(H)
M = int(M)
if M < 45:
    if H == 0:
        H += 23
        M += 60
    else:
        H -= 1
        M += 60
print(H,M-45)