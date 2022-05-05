# class stackelement:
#     def __init__(self,data,next):
#         self.data = data
#         self.next = next
#
# class stack:
#     def __init__(self):
#         self.top = None
#         self.size= 0
#     def push(self,data):
#         if self.top is None:
#             elem = stackelement(data,None)
#             self.top = elem
#             self.size += 1
#         else:
#             elem = stackelement(data,self.top)
#             self.top = elem
#             self.size +=1
#     def pop(self):
#         if self.top is None:
#             return -1
#
#         else:
#             temp = self.top
#             self.top = self.top.next
#             self.size -=1
#             return temp.data
#
#     def peek(self):
#         if self.top is None:
#             return -1
#         else:
#             return self.top.data
#     def empty(self):
#         if self.top is None:
#             return 1
#         else:
#             return 0
#     def length(self):
#         return self.size
# s1 = stack()
# v = int(input())
# for i in range(v):
#     a = input().split(' ')
#     if a[0] == 'push':
#         s1.push(a[1])
#     if a[0] == 'pop':
#         print(s1.pop())
#     if a[0] == 'top':
#         print(s1.peek())
#     if a[0] == 'empty':
#         print(s1.empty())
#     if a[0] == 'size':
#         print(s1.length())




class dequeelement:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right
class deque:
    def __init__(self):
        self.rear = None
        self.front = None
    def insert_rear(self,data):
        if self.rear is None:
            elem = dequeelement(data,None,None)
            self.rear = elem
            self.front = elem
        else:
            elem = dequeelement(data, None, self.rear)
            self.rear.left = elem
            self.rear = elem
    def insert_front(self,data):
        if self.front is None:
            elem = dequeelement(data,None,None)
            self.front = elem
            self.rear = elem
        else:
            elem = dequeelement(data,self.front,None)
            self.front.right = elem
            self.front = elem
    def delete_rear(self):
        if self.rear is None:
            return None
        temp = self.rear
        if self.rear == self.front:
            self.front=self.rear = None
            return temp.data
        else:
            temp = self.rear
            self.rear = self.rear.right
            self.rear.left = None
            return temp.data
    def delete_front(self):
        if self.front is None:
            return None
        temp = self.front
        if self.rear == self.front:
            self.rear = self.front = None
            return temp.data
        else:
            self.front = self.front.left
            self.front.right = None
            return temp.data
    #TODO reverse 구현
    def reverse(self):
        pass
dq = deque()
for i in range(1,6):
    dq.insert_front(i)
for i in range(5):
    print(dq.delete_front())