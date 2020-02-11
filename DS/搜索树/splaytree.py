# 优点：伸展树(splay tree)是一种能自我调整的二叉搜索树(BST)。
# 虽然某一次的访问操作所花费的时间比较长，但是平摊（amortized）
# 之后的访问操作（例如旋转）时间能达到O(logn)的复杂度。
# 对于某一个被访问的节点，在接下来的一段时间内再次频繁访问它
# （90%的情况下是这样的，即符合90-10规则，类似于CPU内或磁盘的cache设计原理）
# 的应用模式来说，伸展树是一种很理想的数据结构。另外一点与其他平衡二叉树的区别是，
# 伸展树不需要存储任何像AVL树中平衡因子(balance factor)那样的平衡信息，可以节省空间的开销。

# 缺点：不像其他平衡二叉树那样即使最坏情况下也能达到O(logn)访问时间，它的最坏情况下只有O(n)，跟单向链表一样。
# 另外，伸展树的查找操作会修改树的结构，这与普通意义上的查找为只读操作习惯不太一样。

# 实现方式：伸展树的实现有两种方式，一是自底向上(bottom-up)，另外一种是自顶向下(top-down)。
# 考虑到实现的难易程度，自顶向下的实现方式比较简单，因为自底向上需要保存已经被访问的节点，
# 而自顶向下可以在搜索的过程中同时完成splay操作。
# 虽然两者得出的树结构不太一样，但是它们的平摊时间复杂度都是O(logn)。
# 两种实现的基本操作就是splay，splay将最后被访问到的节点提升为根节点。

# 在自顶向下(top-down)的实现中，需要将输入的树拆成三颗树，分别为左树L，中树M和右树R。
# 其中M树维护当前还未被访问到的节点，L树中所有节点的值都小于M树中的任何节点值，
# R树中所有节点的值都大于M树中的任何节点值。L树中只需要知道当前的最大节点 (leftTreeMax)，
# 而R树中只需要知道当前的最小节点(rightTreeMin)。左右两棵树的根节点分别可以通过nullNode节点
# （它是leftTreeMax和rightTreeMin的初始值，而且splay过程中变量nullNode本身未变化,只改变它的左右孩子节点）
# 的右和左孩子节点得到，因为leftTreeMax中加入一个新的节点或子树时都是将新的节点作为leftTreeMax的右孩子，
# 而不是左孩子（注意这里的顺序），rightTreeMin跟leftTreeMax相反。自顶向下的zig-zig或zag-zag需要做旋转操作，
# zig-zig的旋转操作叫rotationWithLeftChild,旋转后目标节点的父节点和祖父节点加入R树，
# zag-zag的旋转操作叫rotationWithRightChild,旋转后目标节点的父节点和祖父节点加入L树。
# 另外zig-zag或zag-zig可以分别简化为zig或zag操作，这样可以将zig-zag和zig合二为一，
# 从而只需考虑一种情况，而不需要将两种情况单独考虑。zig操作将目标节点的父节点加入R树，
# zag操作将目标节点的父节点加入L树。注意L和R树中每次加入新节点都需更新变量leftTreeMax或rightTreeMin。
# 自顶向下splay操作的最后一步是重组(re-assemble)：将M树的左孩子设置为L树的根节点，
# 将M树的右孩子设置为R树的根节点，然后M树原来的左孩子成为leftTreeMax的右孩子，M树原来的右孩子成为rightTreeMin的左孩子。



class SplayTree(object):
    class __SplayNode(object):
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem

            if (self.key != None):
                yield self.key

            if self.right != None:
                for elem in self.right:
                    yield elem

        # 迭代的是Node类型，用于删除结点
        def iternodes(self):
            if self.left != None:
                for elem in self.left.iternodes():
                    yield elem

            if self != None and self.key != None:
                yield self

            if self.right != None:
                for elem in self.right.iternodes():
                    yield elem

        def info(self):
            s = 'Key=' + str(self.key) + ', ' + \
                'LChild=' + str(self.left) + ', ' + \
                'RChild=' + str(self.right)
            print(s)

        def __str__(self):
            return str(self.key)

        def __repr__(self):
            if self != None:
                s_1 = str(self.key)
            else:
                s_1 = 'None'
            if self.left != None:
                s_2 = str(self.left.key)
            else:
                s_2 = 'None'
            if self.right != None:
                s_3 = str(self.right.key)
            else:
                s_3 = 'None'
            return '__SplayNode(' + s_1 + ', ' + s_2 + ', ' + s_3 + ')'

    def __init__(self):
        self.root = None
        self.header = SplayTree.__SplayNode(None)  # For splay()

    # LL
    def singleLeftRotate(self, node):
        k1 = node.left
        node.left = k1.right
        k1.right = node
        return k1

    # RR
    def singleRightRotate(self, node):
        k1 = node.right
        node.right = k1.left
        k1.left = node
        return k1

    # RL
    def doubleLeftRotate(self, node):
        node.left = self.singleRightRotate(node.left)
        return self.singleLeftRotate(node)

    # LR
    def doubleRightRotate(self, node):
        node.right = self.singleLeftRotate(node.right)
        return self.singleRightRotate(node)

    # 伸展运动
    def splay(self, key):
        l = r = self.header
        t = self.root
        if t is None:
            return
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    t = self.singleLeftRotate(t)
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    t = self.singleRightRotate(t)
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break

        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t

    # 和splay操作捆绑的方法
    # 插入
    def insert(self, key):
        if (self.root == None):
            self.root = SplayTree.__SplayNode(key)
            return
        self.splay(key)
        if self.root.key == key:
            # If the key is already there in the tree, don't do anything.
            return
        n = SplayTree.__SplayNode(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if self.root is None or key != self.root.key:
            return None

        # Now delete the root.
        if self.root.left == None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x
        return key

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None

    # 结构信息查询，不与splay操作捆绑
    def getRoot(self):
        return repr(self.root)

    def info(self):
        a = []
        for x in self:
            a.append(x)
        print(a)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

    def __contains__(self, val):
        for x in self:
            if (x == val):
                return True
        return False

    def __len__(self):
        a = []
        for x in self:
            a.append(x)

        return len(a)

    # 求结点高度
    def height(self, node):
        if (node == None):
            return 0
        else:
            m = self.height(node.left)
            n = self.height(node.right)
            return max(m, n) + 1

        # 传回结点的原始信息

    def iternodes(self):
        if self.root != None:
            return self.root.iternodes()
        else:
            return [None]

    # 寻找节点路径
    def findNodePath(self, root, node):
        path = []
        if root == None or root.key == None:
            path = []
            return path

        while (root != node):
            if node.key < root.key:
                path.append(root)
                root = root.left
            elif node.key >= root.key:
                path.append(root)
                root = root.right
            else:
                break
        path.append(root)
        return path

    # 寻找父结点
    def parent(self, root, node):
        path = self.findNodePath(root, node)
        if (len(path) > 1):
            return path[-2]
        else:
            return None

    # 是否左孩子
    def isLChild(self, parent, lChild):
        if (parent.getLeft() != None and parent.getLeft() == lChild):
            return True
        return False

    # 是否右孩子
    def isRChild(self, parent, rChild):
        if (parent.getRight() != None and parent.getRight() == rChild):
            return True
        return False

    # 求某元素是在树的第几层
    # 约定根为0层
    # 这个计算和求结点的Height是不一样的
    def level(self, elem):
        if self.root != None:
            node = self.root
            lev = 0

            while (node != None):
                if elem < node.key:
                    node = node.left
                    lev += 1
                elif elem > node.key:
                    node = node.right
                    lev += 1
                else:
                    return lev
            return -1
        else:
            return -1


if __name__ == '__main__':
    splay = SplayTree()
    a = [20, 30, 40, 120, 13, 39, 38, 40, 18, 101]
    for item in a:
        splay.insert(item)
        print(splay.getRoot())
        print(splay.height(splay.root))
    splay.info()
    print(len(splay))
    for node in splay.iternodes():
        print(splay.findNodePath(splay.root, node), '\n')
    '''
    for item in reversed(a):
        print('remove:', splay.remove(item));
        splay.getRoot();
        print(splay.height(splay.root));
    '''
    print(splay.findMax())
    print(splay.getRoot())
