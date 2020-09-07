# -*- coding:utf-8 -*-

class Transform:
    def trans(self, s, n):
        # write code here
        temp = ''
        for i in range(n):
            if s[i].islower():
                temp = temp + s[i].upper()
            elif s[i].isupper():
                temp = temp + s[i].lower()
            else:
                temp = temp + s[i]

        return ' '.join(temp.split(' ')[::-1])
