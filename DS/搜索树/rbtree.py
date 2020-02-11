# 红黑树（Red–black tree）是一种自平衡二叉查找树，典型的用途是实现关联数组。
# 它可以在O(log n) 时间内做查找，插入和删除，这里的n是树中元素的数目。
# 红黑树相对于AVL树来说，牺牲了部分平衡性以换取插入/删除操作时少量的旋转操作，整体来说性能要优于AVL树。
# 红黑树是每个节点都带有颜色属性的二叉查找树，颜色为红色或黑色。

# 红黑树的五大性质：
#   性质一：节点是红色或者是黑色；
#   性质二：根节点是黑色；
#   性质三：每个叶节点（NIL或空节点）是黑色；
#   性质四：每个红色节点的两个子节点都是黑色的（也就是说不存在两个连续的红色节点）；
#   性质五：从任一节点到其没个叶节点的所有路径都包含相同数目的黑色节点


class RBTreeNode(object):
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
        self.size = None


# 定义红黑树
class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

    # 左旋转
    def LeftRotate(self, T, x):
        y = x.right
        x.right = y.left
        if y.left != T.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # 右旋转
    def RightRotate(self, T, x):
        y = x.left
        x.left = y.right
        if y.right != T.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # 红黑树的插入
    def RBInsert(self, T, z):
        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil
        z.right = T.nil
        z.color = 'red'
        self.RBInsertFixup(T, z)
        return z.key, '颜色为', z.color

    # 红黑树的上色
    def RBInsertFixup(self, T, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.LeftRotate(T, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.RightRotate(T, z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.RightRotate(T, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.LeftRotate(T, z.parent.parent)
        T.root.color = 'black'

    def RBTransplant(self, T, u, v):
        if u.parent == T.nil:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RBDelete(self, T, z):
        y = z
        y_original_color = y.color
        if z.left == T.nil:
            x = z.right
            self.RBTransplant(T, z, z.right)
        elif z.right == T.nil:
            x = z.left
            self.RBTransplant(T, z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBTransplant(T, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBTransplant(T, z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.RBDeleteFixup(T, x)

    # 红黑树的删除
    def RBDeleteFixup(self, T, x):
        while x != T.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.LeftRotate(T, x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.RightRotate(T, w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.LeftRotate(T, x.parent)
                    x = T.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.RightRotate(T, x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.LeftRotate(T, w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.RightRotate(T, x.parent)
                    x = T.root
        x.color = 'black'

    def TreeMinimum(self, x):
        while x.left != T.nil:
            x = x.left
        return x

    # 中序遍历
    def Midsort(self, x):
        if x != None:
            self.Midsort(x.left)
            if x.key != 0:
                print('key:', x.key, 'x.parent:', x.parent.key)
            self.Midsort(x.right)


if __name__ == '__main__':
    nodes = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    T = RBTree()
    for node in nodes:
        print('插入数据', T.RBInsert(T, RBTreeNode(node)))
    print('中序遍历')
    T.Midsort(T.root)
    T.RBDelete(T, T.root)
    print('中序遍历')
    T.Midsort(T.root)
    T.RBDelete(T, T.root)
    print('中序遍历')
    T.Midsort(T.root)
