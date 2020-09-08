#
# ��֤IP��ַ
# @param IP string�ַ��� һ��IP��ַ�ַ���
# @return string�ַ���
#
class Solution:
    def solve(self, IP):
        if '.' in IP:
            for ip in IP.split('.'):
                if ip == '' or ip[0] == '0' or (not 0 <= int(ip) <= 255):
                    return 'Neither'
            return 'IPv4'
        elif ':' in IP:
            for ip in IP.split(':'):
                if ip == '' or (len(ip) > 1 and len(ip) == ip.count('0')):
                    return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'
