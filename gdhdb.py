# 인덱싱 = 하나의 값을 출력 = [indexing_number]
# a = ['a','b',['c','d',['5','6'],'3'],'4']
# print(a[2][3]) #3을 출력
# print(a[2][2][1]) #6을 출력
a = [4,1,3,2]
# a[3] = 6# 3번째 자리에 6을 넣는다
#print(a)
# del a[2] #괄호 없이
# print(a)
#a.remove a 리스트 안에 값을 뺴는 것
# print(a.pop(2), '\t',a) #결과:3 	 [4, 1, 2] a리스트 안에서 어떤위치에 있는 값 추츨
# b = [5,2]
# a.extend(b)
# my_variable = ()
# movie_rank = ('닥터스트레인지','스플릿','럭키')
# a = (1,) #원소가 하나 있을땐 콤마 써야됨(튜플)
# interest = ('삼성전자', 'lg전자', 'sSl하이닉스')
# print(type(interest))
# interest = list(interest)
# print(type(interest))
# temp = ('apple','banana','cake')
# a, b, c = temp
# print(a)
# print(b)
# print(c)
# d = {'apple':'사과','banana':'바나나',"3":"삼"}
# print(d['apple'],d["banana"],d["3"])
# d['peach'] = '복숭아'
# d['apple'] = '배'
# print(d)
# temp = { }
# 아이스크림 = {'메로나':1000,'폴라포':1200,'빵빠레':1800}
# 아이스크림['죠스바']= 1200
# 아이스크림['월드콘']=1500
# # print(아이스크림)
# print('메로나 가격:',아이스크림['메로나'])
# 아이스크림['메로나']=1300
# del 아이스크림['메로나']
# print(아이스크림)
# d = {"메로나":[300,20],'비비빅':[400,3],'죠스바':[250,100]}
# print(d['메로나'][1])
# d['월드콘'] =[500,7]
# print(d)
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# key = list(icecream.values())
# print(sum(key))
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys,vals))
# print(result)
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)