# def solution(new_id):
#     answer = ''
#     new_id = new_id.lower()
#     for i in new_id:
#         if i not in 'qazwxsedcrfvtgbyhnujmikolp.-_1234567890':
#             new_id = new_id.replace(i,'')
#
#     while '..' in new_id:
#         new_id = new_id.replace('..','.')
#
#     new_id = new_id.strip('.')
#     if len(new_id) == 0:
#         new_id = 'a'
#     if len(new_id) > 15:
#         new_id =new_id.replace(new_id[15:],'')
#
#     if new_id[-1:] == '.':
#         new_id = new_id.replace(new_id[-1:],'')
#     if len(answer) < 3:
#         while len(answer) < 3:
#             answer += answer[-1]
#     return answer
# print(solution("...!@BaT#*..y.abcdefghijklm"	))
# def solution(new_id):
#     answer = ''
#     new_id = new_id.lower()
#     s_word = '~!@#$%^&*()=+[{]}:?,<>/'
#     for i in range(len(new_id)):
#         if new_id[i] not in s_word:
#             answer += new_id[i]
#     while '..' in new_id:
#         new_id = new_id.replace('..','.')
#     answer.strip('.')
#     if len(answer) >= 16:
#         answer = answer[:15]
#         if answer.endswith('.'):
#             answer = answer[:-1]
#     if len(answer) <  3:
#         while len(answer) < 3:
#             answer += answer[-1]
#     return answer
class QueueElement:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class queue:
    def __init__(self):
        self.rear = None
        self.front = None
    def enque(self,data):
        if self.rear == None:
            elem = QueueElement(data,None)
            self.front = elem
            self.rear = elem
        else:
            elem = QueueElement(data,None)
            self.rear.next = elem
    def deque(self):
        if self.front == None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            return temp.data
    def reverse(self):
        prev = None
        curr = self.front

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.rear,self.front = self.front,self.rear