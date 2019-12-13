class TreeNode:
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, lc, rc):
        self.key = key
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key):
        if self.root:
            self._put(key, self.root)

        else:
            self.root = TreeNode(key)
        self.size += 1

    def _put(self, key, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, currentNode.leftChild)

            else:
                currentNode.leftChild = TreeNode(key, parent=currentNode)

        else:
            if currentNode.hasRightChild():
                self._put(key, currentNode.rightChild)

            else:
                currentNode.rightChild = TreeNode(key, parent=currentNode)



    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return True
            else:
                return None

        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None

        elif currentNode.key == key:
            return currentNode

        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)

        else:
            return self._get(key, currentNode.rightChild)


    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)

            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                print('Error, key not in tree')

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1

        else:
            print('Error, key not in tree')




    # def spliceOut(self):
    #     if self.isLeaf():
    #         if self.isLeftChild():
    #             self.parent.leftChild = None
    #         else:
    #             self.parent.rightChild = None
    #     elif self.hasAnyChildren():
    #         if self.hasLeftChild():
    #             if self.isLeftChild():
    #                 self.parent.leftChild = self.leftChild
    #             else:
    #                 self.parent.rightChild = self.leftChild
    #             self.leftChild.parent = self.parent
    #
    #         else:
    #             if self.isLeftChild():
    #                 self.parent.leftChild = self.rightChild
    #             else:
    #                 self.parent.rightChild = self.rightChild
    #             self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    # def findMin(self):
    #     current = self
    #     while current.hasLeftChild():
    #         current = current.leftChild
    #     return current

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key


        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                # else:
                #     currentNode.replaceNodeData(currentNode.leftChild.key,
                #                                 currentNode.leftChild.leftChild,
                #                                 currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                # else:
                #     currentNode.replaceNodeData(currentNode.rightChild.key,
                #                                 currentNode.rightChild.leftChild,
                #                                 currentNode.rightChild.rightChild)


    def inorder(self,cur):
        if cur.leftChild:
            self.inorder(cur.leftChild)
        print(cur.key)
        if cur.rightChild:
            self.inorder(cur.rightChild)

    def postorder(self,cur):
        if cur.leftChild:
            self.postorder(cur.leftChild)
        if cur.rightChild:
            self.postorder(cur.rightChild)
        print(cur.key)


    def preorder(self, cur):
        print(cur.key)
        if cur.leftChild:
            self.preorder(cur.leftChild)
        if cur.rightChild:
            self.preorder(cur.rightChild)






tree = BinarySearchTree()

tree.put(5)
tree.put(4)
tree.put(10)

tree.postorder(tree.root)


print('''
    1 - добавить узел
    2 - удалить узел
    3 - найти значение
    4 - прямой ход
    5 - обратный ход
    6 - концевой ход
    7 - выход
''')

while True:
    q = int(input())
    if q == 1:
        tree.put(int(input('Введите значение:')))
    elif q == 2:
        tree.delete(int(input('Введите значение:')))
    elif q == 3:
        print(tree.get(int(input('Введите значение:'))))
    elif q == 4:
        tree.preorder(tree.root)
    elif q == 5:
        tree.postorder(tree.root)
    elif q == 6:
        tree.inorder(tree.root)
    elif q == 7:
        break
