class String:
    # 初始化串
    def __init__(self):
        self.MaxStringSize = 256
        self.chars = ""
        self.length = 0

    # 判断是否为空
    def IsEmpty(self):
        if self.length == 0:
            IsEmpty = True
        else:
            IsEmpty = False
        return IsEmpty

    # 创建串
    def CreateString(self):
        stringSH = input("请输入字符串：")
        if len(stringSH) > self.MaxStringSize:
            print("溢出，超过的部分无法保存")
            self.chars = stringSH[:self.MaxStringSize]
        else:
            self.chars = stringSH

    # 串连接
    def StringConcat(self, strSrc):
        lengthSrc = strSrc.length
        stringSrc = strSrc.chars
        if lengthSrc + len(self.chars) <= self.MaxStringSize:
            self.chars = self.chars + stringSrc
        else:
            print("两个字符的长度之和溢出，超过的部分无法显示")
            size = self.MaxStringSize - len(self.chars)
            self.chars = self.chars + stringSrc[:size]
        print("连接后字符串为：", self.chars)

    # 获取字串
    def SubString(self, iPos, length):
        if iPos > len(self.chars) - 1 or iPos < 0 or length < 1 \
                or (length + iPos) > len(self.chars):
            print("无法获取")
        else:
            substr = self.chars[iPos:iPos + length]
            print("获取的字串为：", substr)

    def GetString(self):
        return self.chars


if __name__ == '__main__':
    S = String()
    print(S.IsEmpty())
    S.CreateString()
    print(S.GetString())
