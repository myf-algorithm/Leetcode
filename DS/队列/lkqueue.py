class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LKQueue(object):
    def __init__(self):
        self.front = Node()
        self.rear = Node()
        self.length = 0

    def get_length(self):
        print(self.length)

    def is_empty(self):
        return self.length == 0

    def pushQueue(self, elem):
        """入队"""
        tmp = Node(elem)
        if self.is_empty():
            self.front = tmp
            self.rear = tmp
        else:
            self.rear.next = tmp
            self.rear = tmp
        self.length += 1

    def popQueue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            del_elem = self.front.data
            self.front = self.front.next
            self.length -= 1
            return del_elem

    def showQueue(self):
        """遍历"""
        if self.is_empty():
            print("Queue is empty!")
        j = self.length
        tmp = self.front
        while j > 0:
            print(tmp.data, end=' ')
            tmp = tmp.next
            j -= 1
        print('')


if __name__ == '__main__':
    lkq = LKQueue()
    lkq.showQueue()
    for i in range(1, 5):
        lkq.pushQueue(i)
    lkq.showQueue()
    lkq.get_length()
    lkq.popQueue()
    lkq.showQueue()
