# a = (input('입력'))
# d =  {'달러':1167,'엔':1.096,'유로':1268,'위안':171}
# # f = a.split()
# # won = d[f[1]] *  int(f[0])
# # print("%.2f"%won,'원')
# a,b= input().split()
# print(a)
# print(b)
# a = int(input())
# b = int(input())
# c = int(input())
# if a>b and a > c:
#     print(a)
# elif b>a and b > c:
#     print(b)
# else:
#     print(c)
# d = {'011':'skt','016':'kt','019':'lgu','010':'알수없음'}
# a = input('휴대전화 번호 입력')
# print('당신은 %s 사용자입니다'%d[a[:3]]
# a = input('우편번호:')
# if a[:3] in ['010','011','012']:
#     print('강북구')
# elif a[:3] in ['013','014','015']:
#     print('도봉구')
# elif a[:3] in ['016','017','018','019']:
#     print('노원구')
# a = input('주민등록번호:')
# if a[7]== '1' or a[7] == '3':
#     print('남자')
# elif a[7]== '2' or a[7] == '4':
#     print('여자')
# a = input('주민등록번호:')
# if a[8:10] in ['01','02','03','04','05','06','07','08']:
#     print('서울입니다')
# else:
#     print('서울이 아닙니다')
# 주민번호 = input("주민등록번호: ")
# 뒷자리 = 주민번호.split("-")[1]
# if 0 <= int(뒷자리[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")
# a = input()
# b =int(a[0])*2 + int(a[1])*3 + int(a[2])*4 + int(a[3])*5 + int(a[4])*6 + int(a[5])*7 + int(a[7])*8 + int(a[8])*9 + int(a[9])*2 + int(a[10])*3 + int(a[11])*4 + int(a[12])*5
#
# print(b)
# c = b%11
# print(c)
# print(11-c)
# if 11-c == int(a[-1]):
#     print('유효')
# else:
#     print('유효x')
# sum= 1
# sum+=2
# print(sum)
# 리스트 = ["가", "나", "다", "라"]
# # for i in range(1,4):
# #     print(리스트[i])
# # for i in 리스트[::-1]:
# #     print(i)
# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i<0:
#         print(i)
# 리스트 = [3, 100, 23, 44]
# for i in 리스트:
#     if i%3 == 0:
#         print(i)
# 리스트 = [13, 21, 12, 14, 30, 18]
# for i in 리스트:
    # if i<20:
    #     if i%3 == 0:
    #         print(i)
    # if i<20 and i%3 == 0:
    #     print(i)
# 리스트 = ["I", "study", "python", "language", "!"]
# for i in 리스트:
#     if len(i) >=3:
#         print(i)
# 리스트 = ["A", "b", "c", "D"]
# for i in 리스트:
#     if i.isupper():
#         print(i)
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# for i in 리스트:
#     print(i.split('.')[0])
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for i in 리스트:
#     if i.split('.')[1] =='h' or i.split('.')[1] =='c':
#         print(i)
# for i in range(1,10):
#     print(i/10)
# for i in range(1,10):
#     if i%2 != 0:
#         print('3 x %d=%d' % (i, 3 * i))
# a = 1
# for i in range(1,11,):
#     a *= i
#     print(a)
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(3-i,price_list[i])
# price_list = [32100, 32150, 32000, 32500]
# for i in range(1,len(price_list)):
# #     print(90+i*10,price_list[i])
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):        # i 0 = 0~2
#     print(my_list[i],my_list[i+1],my_list[i+2])
# my_list = ["가", "나", "다", "라"]
# for i in range(1,len(my_list)):
#     print(my_list[-i],my_list[-i-1])
# my_list = [100, 200, 400, 800]
# for i in range(len(my_list)-1):
#     print(my_list[i+1]-my_list[i])
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list)-2):         #i=0 ~ 3
#      print((my_list[i]+my_list[i+1]+my_list[i+2])/3)
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(len(high_prices)):
#     volatility.append(high_prices[i] - low_prices[i])
# print(volatility)
# apart = [['101호','102호'],['201호','202호'],['301호','302호']]
# stock = [['시가',100,200,300],['종가',80,210,330]]
# stock = {stock[0][0]:stock[0][1],stock[1][0]:stock[1][1]}
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
# #     for x in range(len(apart)[0])):
#         print(apart[i][x])
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(1,len(apart)+1):
#     for j in range(len(apart[0])):
#         print(apart[-i][j])
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(1,len(apart)+1):
#     for j in range(len(apart[0])):
#         print(apart[-i][j])
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(1,len(apart)+1):
#     for j in range(len(apart[0])):
#         print(apart[-i][-j])
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     for j in range(len(apart[0])):
#         print(apart[i][j])
#     print('-----')
    
