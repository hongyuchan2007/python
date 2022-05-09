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
        a = None
        b = self.rear
        c = self.front

        while b:
            self