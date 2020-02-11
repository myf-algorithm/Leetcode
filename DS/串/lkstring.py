class StringNode:
    # 初始化串节点的函数
    def __init__(self):
        self.data = None
        self.next = None


class LKString:
    def __init__(self):
        self.head = StringNode()
        self.tail = self.head
        self.length = 0

    # 创建一个链串的函数
    def CreateString(self):
        stringSH = input("请输入一个字符串：")
        print(stringSH)
        while self.length < len(stringSH):
            Tstring = StringNode()
            Tstring.data = stringSH[self.length]
            self.tail.next = Tstring
            self.tail = Tstring
            self.length += 1

    # 复制的函数
    def StringCopy(self, strSrc):
        self.head = strSrc.head
        self.tail = strSrc.tail
        self.length = strSrc.length

    def StringConcat(self, strSrc):
        self.tail.next = strSrc.head.next
        self.tail = strSrc.tail
        self.length += strSrc.length

    def GetString(self):
        cur = self.head.next
        while cur.next != None:
            print(cur.data, end='')
            cur = cur.next
        print(cur.data, end='')


if __name__ == '__main__':
    LKS = LKString()
    LKS.CreateString()
    LKS.GetString()