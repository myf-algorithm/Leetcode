class dlNode:
    def __init__(self, key, val, cnt=0):
        self.val = [key, val, cnt]  # ����ֵ�����ʴ���
        self.pre = None
        self.nxt = None


class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}  # ͨ��key��������ڵ㣬key:node
        self.c = capacity  # �ֵ�����
        self.head = dlNode(1, 1, float('inf'))  # ͷ�ڵ㣬������ʴ���������
        self.tail = dlNode(-1, -1, float('-inf'))  # β�ڵ㣬������ʴ���������
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def _refresh(self, node, cnt):  ##�����������Խڵ�node���Է��ʴ���cnt���¶�����λ��
        pNode, nNode = node.pre, node.nxt  # ��ǰ�ڵ��ǰ��ڵ�
        if cnt < pNode.val[2]:  # ������ʴ���С��ǰ�ڵ�ķ��ʴ������������λ��
            return
        pNode.nxt, nNode.pre = nNode, pNode  # ��ǰ��������������nodeλ��
        while cnt >= pNode.val[2]:  # ǰ�Ƶ������ܿ�ǰ��λ�ú����
            pNode = pNode.pre
        nNode = pNode.nxt
        pNode.nxt = nNode.pre = node
        node.pre, node.nxt = pNode, nNode

    def get(self, key: int) -> int:
        if self.c <= 0 or key not in self.cache:  # �������<=0����key�����ֵ��У�ֱ�ӷ���-1
            return -1
        node = self.cache[key]  # ͨ���ֵ��ҵ��ڵ�
        _, value, cnt = node.val  # ͨ���ڵ�õ�key��value��cnt
        node.val[2] = cnt + 1  # ���ʴ���+1
        self._refresh(node, cnt + 1)  # ˢ��λ��
        return value

    def put(self, key: int, value: int) -> None:
        if self.c <= 0:  # ��������<=0
            return
        if key in self.cache:  # �����ֵ��У���Ҫ������value��ͬʱ���ʴ���+1ˢ��λ��
            node = self.cache[key]
            _, _, cnt = node.val
            node.val = [key, value, cnt + 1]  # ������ֵ
            self._refresh(node, cnt + 1)
        else:
            if len(self.cache) >= self.c:  # �����������������β��Ԫ��
                tp, tpp = self.tail.pre, self.tail.pre.pre
                self.cache.pop(tp.val[0])  # ���ֵ��޳�β�ڵ�
                tpp.nxt, self.tail.pre = self.tail, tpp  # ��β����������ԭβ�ڵ�
            node = dlNode(key, value)  # �½��ڵ㣬�����뵽��β����ˢ����λ��
            node.pre, node.nxt = self.tail.pre, self.tail
            self.tail.pre.nxt, self.tail.pre = node, node
            self.cache[key] = node
            self._refresh(node, 0)


class Solution:
    def LFU(self, operators, k):
        lfu_t = [[] for i in range(100)]
        dic = {}
        res = []
        for ops in operators:
            opt = ops[0]
            if opt == 1:
                if ops[1] not in dic:
                    dic[ops[1]] = []
                    dic[ops[1]].append(ops[2])
                    dic[ops[1]].append(1)
                    lfu_t[1].append(ops[1])
                else:
                    dic[ops[1]][0] = ops[2]
                    lfu_t[dic[ops[1]][1]].remove(ops[1])
                    dic[ops[1]][1] += 1
                    lfu_t[dic[ops[1]][1]].append(ops[1])
                if len(dic) > k:
                    for key in lfu_t:
                        if len(key) > 0:
                            key_key = key.pop(0)
                            dic.pop(key_key)
                            break
            elif opt == 2:
                if ops[1] not in dic:
                    val = -1
                else:
                    val = dic[ops[1]][0]
                    lfu_t[dic[ops[1]][1]].remove(ops[1])
                    dic[ops[1]][1] += 1
                    lfu_t[dic[ops[1]][1]].append(ops[1])
                res.append(val)
        return res
