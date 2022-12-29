# B-Tree是为磁盘等外存储设备设计的一种平衡查找树。因此在讲B-Tree之前先了解下磁盘的相关知识。
# 系统从磁盘读取数据到内存时是以磁盘块（block）为基本单位的，位于同一个磁盘块中的数据会被一次性读取出来，而不是需要什么取什么。
# InnoDB存储引擎中有页（Page）的概念，页是其磁盘管理的最小单位。InnoDB存储引擎中默认每个页的大小为16KB，
# 可通过参数innodb_page_size将页的大小设置为4K、8K、16K，在MySQL中可通过如下命令查看页的大小：
# mysql> show variables like 'innodb_page_size';
# 而系统一个磁盘块的存储空间往往没有这么大，因此InnoDB每次申请磁盘空间时都会是若干地址连续磁盘块来达到页的大小16KB。
# InnoDB在把磁盘数据读入到磁盘时会以页为基本单位，在查询数据时如果一个页中的每条数据都能有助于定位数据记录的位置，
# 这将会减少磁盘I/O次数，提高查询效率。
# B-Tree结构的数据可以让系统高效的找到数据所在的磁盘块。为了描述B-Tree，首先定义一条记录为一个二元组[key, data] ，
# key为记录的键值，对应表中的主键值，data为一行记录中除主键外的数据。对于不同的记录，key值互不相同。

# 一棵m阶的B-Tree有如下特性：
# 1. 每个节点最多有m个孩子。
# 2. 除了根节点和叶子节点外，其它每个节点至少有Ceil(m/2)个孩子。
# 3. 若根节点不是叶子节点，则至少有2个孩子
# 4. 所有叶子节点都在同一层，且不包含其它关键字信息
# 5. 每个非终端节点包含n个关键字信息（P0,P1,…Pn, k1,…kn）
# 6. 关键字的个数n满足：ceil(m/2)-1 <= n <= m-1
# 7. ki(i=1,…n)为关键字，且关键字升序排序。
# 8. Pi(i=1,…n)为指向子树根节点的指针。P(i-1)指向的子树的所有节点关键字均小于ki，但都大于k(i-1)


class Entity(object):
    '''数据实体'''

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Node(object):
    '''B树的节点'''

    def __init__(self):
        self.parent = None
        self.entitys = []
        self.childs = []

    def find(self, key):
        '''通过key查找并返回一个数据实体'''
        for e in self.entitys:
            if key == e.key:
                return e

    def delete(self, key):
        '''通过key删除一个数据实体,并返回它和它的下标(下标,实体)'''
        for i, e in enumerate(self.entitys):
            if e.key == key:
                del self.entitys[i]
                return (i, e)

    def isLeaf(self):
        '''判断该节点是否是一个叶子节点'''
        return len(self.childs) == 0

    def addEntity(self, entity):
        '''添加一个数据实体'''
        self.entitys.append(entity)
        self.entitys.sort(key=lambda x: x.key)

    def addChild(self, node):
        '''添加一个子节点'''
        self.childs.append(node)
        node.parent = self
        self.childs.sort(key=lambda x: x.entitys[0].key)


class Tree(object):
    '''B树'''

    def __init__(self, size=6):
        self.size = size
        self.root = None
        self.length = 0

    def add(self, key, value=None):
        '''插入一条数据到B树'''
        self.length += 1
        if self.root:
            current = self.root
            while not current.isLeaf():
                for i, e in enumerate(current.entitys):
                    if e.key > key:
                        current = current.childs[i]
                        break
                    elif e.key == key:
                        e.value = value
                        self.length -= 1
                        return
                else:
                    current = current.childs[-1]
            current.addEntity(Entity(key, value))
            if len(current.entitys) > self.size:
                self.__spilt(current)
        else:
            self.root = Node()
            self.root.addEntity(Entity(key, value))

    def get(self, key):
        '''通过key查询一个数据'''
        node = self.__findNode(key)
        if node:
            return node.find(key).value

    def delete(self, key):
        '''通过key删除一个数据项并返回它'''
        node = self.__findNode(key)
        if node:
            i, e = node.delete(key)
            if not node.isLeaf():
                child = node.childs[i]
                j, entity = child.delete(child.entitys[-1].key)
                node.addEntity(entity)
                while not child.isLeaf():
                    node = child
                    child = child.childs[j]
                    j, entity = child.delete(child.entitys[-1].key)
                    node.addEntity(entity)
            self.length -= 1
            return e.value

    def isEmpty(self):
        return self.length == 0

    def __findNode(self, key):
        '''通过key值查询一个数据在哪个节点,找到就返回该节点'''
        if self.root:
            current = self.root
            while not current.isLeaf():
                for i, e in enumerate(current.entitys):
                    if e.key > key:
                        current = current.childs[i]
                        break
                    elif e.key == key:
                        return current
                else:
                    current = current.childs[-1]
            if current.find(key):
                return current

    def __spilt(self, node):
        '''
        分裂一个节点，规则为:
        1、中间的数据项移到父节点
        2、新建一个右兄弟节点，将中间节点右边的数据项移到新节点
        '''
        middle = int(len(node.entitys) / 2)
        top = node.entitys[middle]
        right = Node()
        for e in node.entitys[middle + 1:]:
            right.addEntity(e)
        for n in node.childs[middle + 1:]:
            right.addChild(n)
        node.entitys = node.entitys[:middle]
        node.childs = node.childs[:middle + 1]
        parent = node.parent
        if parent:
            parent.addEntity(top)
            parent.addChild(right)
            if len(parent.entitys) > self.size:
                self.__spilt(parent)
        else:
            self.root = Node()
            self.root.addEntity(top)
            self.root.addChild(node)
            self.root.addChild(right)


if __name__ == '__main__':
    t = Tree(4)
    t.add(20)
    t.add(40)
    t.add(60)
    t.add(70, 'c')
    t.add(80)
    t.add(10)
    t.add(30)
    t.add(15, 'python')
    t.add(75, 'java')
    t.add(85)
    t.add(90)
    t.add(25)
    t.add(35, 'c#')
    t.add(50)
    t.add(22, 'c++')
    t.add(27)
    t.add(32)

    print(t.get(15))
    print(t.get(75))
    print(t.delete(35))
    print(t.delete(22))
    t.add(22, 'lua')
    print(t.get(22))
    print(t.length)
