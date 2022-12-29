# coding:utf-8
# 哈夫曼树：带权路径长度最短的树。
# 哈夫曼编码：使用更短的编码表示高频字符，使平均字符编码长度减少，达到数据压缩的效果。
#   解码时：每个字符的编码互不为前缀码，因此不会出现歧义。

# 一般可以按下面步骤构建：
# 1，将所有左，右子树都为空的作为根节点。
# 2，在森林中选出两棵根节点的权值最小的树作为一棵新树的左，右子树。
#   且置新树的附加根节点的权值为其左，右子树上根节点的权值之和。
#   注意，左子树的权值应小于右子树的权值。
# 3，从森林中删除这两棵树，同时把新树加入到森林中。
# 4，重复2，3步骤，直到森林中只有一棵树为止，此树便是哈夫曼树。


class TreeNode(object):
    def __init__(self, data):
        # 传入的数据是一个元组（字符，对应的频数）
        self.char = data[0]
        self.frequency = data[1]
        self.leftChild = None
        self.rightChild = None
        self.code = ""  # 记录该节点的哈夫曼编码


# 定义森林F中各树的根节点
# 主要涉及的操作有：
# 1，去除F中的某个节点：pop()
# 2，添加新引入的节点：add()


class Forest(object):
    def __init__(self, dataSet):
        q = []  # 定义一个列表用于存储初始节点
        # 依次将初始传入的字符节点作为初始森林中的独立森林节点
        for data in dataSet:
            q.append(TreeNode(data))
        self.queue = q

        # 定义当前森林中节点数量
        self.size = len(self.queue)

    # 定义森林中的出队（去除）操作
    def pop(self):
        self.size -= 1  # 当前队列大小减一
        return self.queue.pop(0)  # 去除队列中的第一个节点元素

    # 定义森林中的节点入队（添加）操作
    def add(self, newNode):
        # 在当前森林中引入一个新节点
        def AddnewNodeToForest(queue, nodeNew):
            # 如果当前队列为空，则直接返回这个新节点作为队列元素
            if len(queue) == 0:
                return [nodeNew]

            # 如果当前队列中所有节点的频数都比新节点小，则直接将该节点加入到队尾
            if queue[len(queue) - 1].frequency < nodeNew.frequency:
                return queue + [nodeNew]

            # 依次比较新节点与队列中节点的频数，按照频数从小到大插入新节点
            for i in range(len(queue)):
                if queue[i].frequency >= nodeNew.frequency:
                    return queue[:i] + [nodeNew] + queue[i:]

        self.queue = AddnewNodeToForest(self.queue, newNode)
        self.size += 1


# 统计传入字符串中各个字符的频数，并将统计结果按照频数排序
def StatisticsChar(string):
    dict = {}
    for char in string:
        if not char in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return sorted(dict.items(), key=lambda x: x[1])


# 根据传入的Forest节点队列依次产生哈夫曼树
def HuffmanTree(Forest):
    # 构造哈夫曼树结束条件：直到森林节点队列中只剩下一个节点
    while Forest.size != 1:
        # 取出节点队列中权值第一小和第二小的节点
        first_small = Forest.pop()
        second_small = Forest.pop()

        # 定义引入新的节点，其权值为第一小和第二小的权值之和，且第一小和第二小分别作为新节点的左右孩子节点
        newNode = TreeNode([None, first_small.frequency + second_small.frequency])
        newNode.leftChild = first_small
        newNode.rightChild = second_small
        Forest.add(newNode)
    return Forest.pop()


# 定义两个字典分别记录字符转换为哈夫曼编码的结果以及哈夫曼编码转为字符的结果
CharToHuffman = {}
HuffmanToChar = {}


# 根据构建的哈夫曼树进行哈夫曼编码
def HuffmanCode(Node, x):
    if Node:
        # 当前节点与其左子结点的边用'0'表示
        HuffmanCode(Node.leftChild, x + '0')
        Node.code += x
        if Node.char:
            CharToHuffman[Node.char] = Node.code
            HuffmanToChar[Node.code] = Node.char
        # 当前节点与左子节点的边用'1'表示
        HuffmanCode(Node.rightChild, x + '1')


# 对传入的字符进行哈夫曼编码
def TransEncode(string):
    global CharToHuffman
    transcode = ""
    for char in string:
        transcode += CharToHuffman[char]
    return transcode


# 将传入的哈夫曼编码解码为字符串
def TransDecode(huffmancode):
    global HuffmanToChar
    code = ""
    result = ""
    for char in huffmancode:
        code += char
        if code in HuffmanToChar:
            result += HuffmanToChar[code]
            code = ""
    return result


if __name__ == '__main__':
    string = 'a' * 5 + 'b' * 27 + 'c' * 2 + 'd' * 11 + 'f' * 10 + 'e' * 8
    forest = Forest(StatisticsChar(string))
    huffmanTree = HuffmanTree(forest)
    HuffmanCode(huffmanTree, '')

    print('原始字符串：\n', string)
    print('\n字符对应的霍夫曼编码：', CharToHuffman)
    print('\n哈夫曼编码解码为对应的字符：', HuffmanToChar)
    print('\n将原始字符串进行哈夫曼编码的结果：')
    huffmanCode = TransEncode(string)
    print(huffmanCode)
    print('\n将哈夫曼编码结果进行解码的结果：')
    huffmanTostring = TransDecode(huffmanCode)
    print(huffmanTostring)
