# 散列表又叫哈希表（Hash Table）：是根据键值(Key-value)而直接进行访问的数据结构。
# 槽：散列表的每一个位置叫做槽，能够存放一个数据项，并以从0开始递增的整数命名。
# 散列函数：某个数据项与在散列表中存储它的槽之间的映射叫做散列函数。
#       散列函数可以将任意一个数据项存储到集合中并返回一个介于槽命名区间内的，0与m-1(m为槽数)之间的整数。
#       散列函数包括：除留余数法(求余)、折叠法、平方取中法、随机数法、数字分析法、直接寻址法等。
#       散列函数必须足够高效，以防止它成为占据存储空间和搜索进程的主要部分。
# 完美散列函数：对于一组给定的数据项，如果散列函数可将每个数据项都映射到不同的槽中，那么这样的散列函数叫做完美散列函数。
# 负载因子：一般把槽被占据的比例叫做负载因子，负载因子𝛌 = 数据项个数/散列表的大小。
# 冲突：由于散列函数的原因，导致两个甚至多个数据存储在同一个槽中，这种情况被称为冲突。

# 处理哈希冲突的方法：
# 1.开放寻址：
#   线性探测：通过系统地向后搜索每一个槽，这种实现开放地址的技术叫做线性探测。线性探测法的一个缺点是产生集中的趋势。
#       解决集中问题的一种方法：是扩展线性探测技术，不再按顺序一个一个地寻找新槽，而是跳过一些槽(N个N个地寻找新槽)，
#           这样能更加平均地分配出现冲突的数据，进而潜在地减少集中问题出现的次数。
#       再散列：这种冲突时为数据寻找新槽的进程被称作再散列，ehash(pos) = (pos + skip) % sizeoftable。
#           需要注意的一点是，选择跳过的槽的个数必须保证所有槽最终都能被遍历。否则，有些槽将会被闲置。
#           为了保证这一点，通常建议将槽的数目设置成质数。
#       解决集中问题的另一种方法：是二次探测法，这种方法不是每次在冲突中选择跳过固定个数的槽，
#           而是使用一个再散列函数使每次跳过槽的数量会依次增加1,3,5,7,9使用一个连续的完全平方数数列作为它的跳跃值。
# 2.链地址法：
#       链能允许多个数据填在散列表中的同一个位置上。
#       当冲突发生时，数据还是填在本应该位于的槽中。
#       但随着同一个槽中填入数据的增多，搜索的难度也随之增加。

# 映射：以一个密钥与一个数据值相关联的无序集合作为结构。映射中的密钥都是独特的，以保证和数据值之间的一一对应关系。
# 映射相关操作：
# 1、map()产生一个新的空映射，返回一个空映射的集合。
# 2、put(key, val)向映射中添加一个新的密钥-数据值对。若密钥已存在，则将旧数据替换为新数据。
# 3、get(key)给定一个key值，返回关联的数据，若不存在，则返回None。
# 4、del从映射中删除一个密钥-数据值对，声明形式为del map[key]。
# 5、len()返回映射中存储的密钥-数据值对的个数。
# 6、in当表述是key in map，返回True否则返回False。


class HashTable(object):
    # 用两个列表来实现映射的数据结构类型。其中一个称为slots(槽)，用来存储key，另一个称为data，用来存储数据值。
    def __init__(self):
        self.size = 11  # 槽数
        self.slots = [None] * self.size  # 利用列表实现一个散列表，每一个元素都被初始化为None。
        self.data = [None] * self.size  # 初始化散列表槽为None

    # 向映射中添加一个新的密钥-数据值对。如果密钥已存在，则将旧数据值替换为新的。
    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))  # 获取散列值作为索引
        if self.slots[hashvalue] == None:  # 若该索引位置为空，则
            self.slots[hashvalue] = key  # 在该索引位置放入key及data
            self.data[hashvalue] = data
        else:  # 若该索引位置不为空，则
            if self.slots[hashvalue] == key:  # 若该索引位置已存在的key值与待处理key值相同，则
                self.data[hashvalue] = data  # 将旧数据值替换为新数据
            else:  # 若该索引位置已存在的key值与待处理key值不同，则
                nextslot = self.rehash(hashvalue, len(self.slots))  # 线性探测下一个槽
                # 若下一个槽的索引位置不为空，并且已存在的key值与待处理key值不同，则
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))  # 继续探测下一个空槽
                if self.slots[nextslot] == None:  # 若下一个槽的索引位置为空，则
                    self.slots[nextslot] = key  # 在该索引位置放入key及data
                    self.data[nextslot] = data
                else:  # 若下一个槽的索引位置已存在的key值与待处理key值相同，则
                    self.data[nextslot] = data  # 将旧数据值替换为新数据

    # 散列函数，获取散列值作为索引
    def hashfunction(self, key, size):
        # 求余，将要存储的数据项与散列表的大小相除，返回余数作为这个数据项的散列值
        return key % size

    # 再散列函数，线性探测向后搜索每一个槽，直到遇到第一个空槽。
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size  # 求余

    # 根据给定的key值，返回关联的数据，若不存在，返回None
    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))  # 获取散列值作为索引
        data = None
        stop = False
        found = False
        position = startslot
        # 若该索引位置不为空，也尚未找到，且没有停止继续查找，则继续循环搜索
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:  # 若找到对应key，则
                found = True
                data = self.data[position]  # 获取对应data
            else:  # 若没找到对应key，则
                position = self.rehash(position, len(self.slots))  # 线性探测下一个槽
                if position == startslot:  # 若依次向下查找一遍后，又循环查找到初始槽，则
                    stop = True  # 停止查找，已全部查找了，说明没有这个key。
        return data

    # 运算符__getitem__和__setitem__允许使用“[]”对字典进行访问。这表示一旦一个散列表被建立，我们所熟悉的索引操作符都将是可用的。
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


if __name__ == '__main__':
    ha = HashTable()  # 实例化散列表类
    ha.put(0, 'haha')  # put()添加数据
    print(ha.get(0))  # get()获取
    print(ha[0])  # __getitem__()获取
    ha[1] = 'hehe'  # __setitem__()设置
    print(ha.slots)  # 存储key的list
    print(ha.data)  # 存储data的list
