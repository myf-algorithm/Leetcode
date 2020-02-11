# AVL树是带有平衡条件的二叉搜索树，一般要求每个节点的左子树和右子树的高度最多差1(空树的高度定义为-1)。
# 在高度为h的AVL树中，最少的节点数S(h)由S(h)=S(h-1)+S(h-2)+1得出，其中S(0)=1，S(1)=2。
# AVL树的查询、插入删除的时间复杂度均为O(logn)。


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def find(self, key):
        if not self.root:
            return None
        else:
            return self._find(key, self.root)

    def _find(self, key, node):
        if not node:
            return None
        elif key < node.data:
            return self._find(key, node.left)
        elif key > node.data:
            return self._find(key, node.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    # 在node节点的左孩子k1的左子树添加了新节点，左旋转，LL旋转
    def singleLeftRotate(self, node):
        # k1为node的left节点
        k1 = node.left
        # 将node节点的左指针指向k1的右孩子
        node.left = k1.right
        # k1的右孩子指向node
        k1.right = node
        # 更新node的平衡因子
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        # 更新k1的平衡因子
        k1.height = max(self.height(k1.left), node.height) + 1
        # 返回k1
        return k1

    # 在node节点的右孩子k1的右子树添加了新节点，右旋转，RR旋转
    def singleRightRotate(self, node):
        # k1为node的right节点
        k1 = node.right
        # 将node节点的右指针指向k1的左孩子
        node.right = k1.left
        # k1的左孩子指向node
        k1.left = node
        # 更新node的平衡因子
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        # 更新k1的平衡因子
        k1.height = max(self.height(k1.right), node.height) + 1
        # 返回k1
        return k1

    # 在node节点的左孩子的右子树添加了新节点，先左后右，LR旋转
    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    # 在node节点的右孩子的左子树添加了新节点，先右后左，RL旋转
    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        if node is None:
            node = TreeNode(key)
        elif key < node.data:
            node.left = self._insert(key, node.left)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if key < node.left.data:  # 在node节点的左孩子k1的左子树添加了新节点，左旋转，LL旋转
                    node = self.singleLeftRotate(node)
                else:  # 在node节点的左孩子的右子树添加了新节点，先左后右，LR旋转
                    node = self.doubleLeftRotate(node)
        elif key > node.data:
            node.right = self._insert(key, node.right)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if key > node.right.data:  # 在node节点的右孩子k1的右子树添加了新节点，右旋转，RR旋转
                    node = self.singleRightRotate(node)
                else:  # 在node节点的右孩子的左子树添加了新节点，先右后左，RL旋转
                    node = self.doubleRightRotate(node)
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def delete(self, key):
        if self.root is None:
            raise KeyError('Error,empty tree')
        else:
            self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            raise KeyError('Error,key not in tree')
        elif key < node.data:
            node.left = self._delete(key, node.left)
            if (self.height(node.right) - self.height(node.left)) == 2:
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.singleRightRotate(node)
                else:
                    node = self.doubleRightRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif key > node.data:
            node.right = self._delete(key, node.right)
            if (self.height(node.left) - self.height(node.right)) == 2:
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.singleLeftRotate(node)
                else:
                    node = self.doubleLeftRotate(node)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        elif node.left and node.right:
            if node.left.height <= node.right.height:
                minNode = self._findMin(node.right)
                node.key = minNode.key
                node.right = self._delete(node.key, node.right)
            else:
                maxNode = self._findMax(node.left)
                node.key = maxNode.key
                node.left = self._delete(node.key, node.left)
            node.height = max(self.height(node.left), self.height(node.right)) + 1
        else:
            if node.right:
                node = node.right
            else:
                node = node.left
        return node


# 根据序列产生一个AVL树
def generate_AVL_tree(seq):
    tree = AVLTree()
    for item in seq:
        tree.insert(item)
    return tree.root


# AVL树的先序遍历
def preorder(seq):
    list1 = []
    node1 = generate_AVL_tree(seq)

    def recurse(node2):
        if node2:
            list1.append(node2.data)
            recurse(node2.left)
            recurse(node2.right)

    recurse(node1)
    return list1


# AVL树的中序遍历
def inorder(seq):
    list1 = []
    node1 = generate_AVL_tree(seq)

    def recurse(node2):
        if node2:
            recurse(node2.left)
            list1.append(node2.data)
            recurse(node2.right)

    recurse(node1)
    return list1


# AVL树的后序遍历
def postorder(seq):
    list1 = []
    node1 = generate_AVL_tree(seq)

    def recurse(node2):
        if node2:
            list1.append(node2.data)
            recurse(node2.right)
            recurse(node2.left)

    recurse(node1)
    return list1


if __name__ == '__main__':
    seq = [10, 1, 3, 4, 5, 6, 7, 8, 9]
    print(inorder(seq))
