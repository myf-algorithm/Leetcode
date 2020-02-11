def encodeAndDecode(string, mode):
    result = ''
    for i in string:
        code = ord(i)
        if 48 <= code <= 57:  # 字符为数字时
            result += chr(48 + (code - 48 - mode) % 10)
        elif 65 <= code <= 90:  # 字符为大写字母时
            result += chr(97 + (code - 65 - mode) % 26)
        elif 97 <= code <= 122:  # 字符为小写字母时
            result += chr(65 + (code - 97 - mode) % 26)
        else:  # 其他字符
            result += i
    return result


try:
    while True:
        print(encodeAndDecode(input(), -1))
        print(encodeAndDecode(input(), 1))
except Exception:
    pass
