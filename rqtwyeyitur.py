# # # int = ['0','1','2','3','4','5','6','7','8','9']
# # #
# # # def solution(s):
# # #     if len(s) == 4 or len(s) == 6:
# # #     return False
# # #
# # #     v = []
# # #     for i in s:
# # #         v.append(i)
# # #     for j in range(len(v)):
# # #         if v[j] not in int:
# # #             answer = False
# # #             break
# # #         if v[j] in int:
# # #             answer = True
# # #
# # #     return answer
# # #
# # # print(solution('312343'))
# #
# #
# #
# #
# #
# #
# #
# #
# # def solution(s):
# #     if len(s) == 4 or len(s) == 6:
# #         for i in s:
# #             if 48 < ord(i) or ord(i) > 57:
# #
# #                 return False
# #         return True
# #     return False
# #
# # def solution(s):
# #     if len(s) == 4 or len(s) == 6:
# #         if s.isdigit():
# #             return True
# #     return False
# #
# #
# #
# #
# #     return False
#
#
# class Fourcal:
#
#
#     def __init__(self):
#
#         self.result = 0
#
#     def add(self,num1,num2):
#         self.result = num1+num2
#         return self.result
#
#     # def sub(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#         return num1 - num2
#
#     def mul(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#         return num1 * num2
#     def div(self,a,b):
#         self.a = a
#         self.b = b
#         return a / b
# call = Fourcal()
# print(call.div(10,3))
#
class stackelement:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        if self.top is None:
            elem = stackelement(data,None)
            self.top = elem
        else:
            elem = stackelement(data,self.top)
            self.top = elem
    def pop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            return temp.data
    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data





