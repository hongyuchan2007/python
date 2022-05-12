class tree_node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right


class binary_tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        node = tree_node(data,None,None)
        if self.root == None:
            self.root = node
        else:
            curr = self.root
            while True:
                if curr.data > node.data:
                    if curr.left == None:
                        curr.left = node
                        return
                    curr = curr.left
                elif curr.data < node.data:
                    if curr.right == None:
                        curr.right = node
                        return
                    curr = curr.right



    def delete(self,data):
        if self.root == None:
            return None
        else:
            curr = self.root
            pcurr = None
            while True:
                if curr.data == data:
                    #1. curr의 자식노드가 한개도 없을경우
                    if curr.left == None and curr.right == None:
                        if pcurr.left == curr:
                            pcurr.left =  None
                        elif pcurr.right == curr:
                            pcurr.right = None

                    #2. curr의 자식노드가 한개 있을겨우
                    elif curr.left == None and curr.right != None:
                        if pcurr.left == curr:
                            pcurr.left = curr.right
                        else:
                            pcurr.right = curr.right
                    elif curr.left != None and curr.right == None:
                        if pcurr.right == curr:
                            pcurr.right = curr.left
                        else:
                            pcurr.left = curr.left
                    else:

                        r_curr = curr.left
                        r_pcurr = curr.left
                        while r_curr.right:
                            r_pcurr = r_curr
                            r_curr = r_curr.right
                        curr.data = r_curr.data
                        r_pcurr.right = None
                    return

                elif curr.data > data:
                    pcurr = curr
                    curr = curr.left
                else:
                    pcurr = curr
                    curr =curr.right
        #전위순회(본인 왼쪽 오른쪽)
    def preorder(self,node):
        if node is not None:
            print(node, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    #중위 (왼쪽 본인 오른쪽)
    def incorder(self,node):
        if node is not None:
            self.incorder(node.left)
            print(node, end=' ')
            self.incorder(node.right)

    #후위순회(왼쪽 오른쪽 본인)
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node, end=' ')
