class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LKStack(object):
    def __init__(self):
        self.top = Node(None)
        self.count = 0

    def get_length(self):
        """获取栈的长度"""
        print(self.count)
        return self.count

    def get_top(self):
        """获取栈顶元素"""
        print(self.top.data)
        return self.top.data

    def is_empty(self):
        return self.count == 0

    def push(self, elem):
        """进栈"""
        tmp = Node(elem)
        if self.is_empty():
            self.top = tmp
        else:
            # 添加栈顶节点
            tmp.next = self.top
            self.top = tmp
        self.count += 1

    def pop(self):
        """出栈"""
        if self.is_empty():
            print("Stack is empty!")
        else:
            self.count -= 1
            elem = self.top.data
            # 移除栈顶节点
            self.top = self.top.next
            return elem

    def show_stack(self):
        """从栈顶开始显示各个节点的值"""
        if self.is_empty():
            print("Stack is empty!")
        else:
            j = self.count
            tmp = self.top
            while j > 0 and tmp:
                if j == 1:
                    print(tmp.data)
                else:
                    print(tmp.data, end=' ')
                    tmp = tmp.next
                j -= 1


if __name__ == '__main__':
    lks = LKStack()
    for i in range(1, 5):
        lks.push(i)
    lks.show_stack()
    lks.get_length()
    lks.pop()
    lks.show_stack()
    lks.get_top()
