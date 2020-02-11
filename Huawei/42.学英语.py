def numToEnghlish(num):
    if num == 0:
        return []
    if num < 20:
        return [one[num - 1]]
    if num < 100:
        return [two[num // 10 - 2]] + numToEnghlish(num % 10)
    if num < 1000:
        return [one[num // 100 - 1]] + ['hundred', 'and'] + numToEnghlish(num % 100)
    for i, word in enumerate(('thousand', 'million', 'billion'), 1):
        if num < 1000 ** (i + 1):
            return numToEnghlish(num // 1000 ** i) + [word] + numToEnghlish(num % 1000 ** i)


try:
    while True:
        one = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
               'thirteen', 'fourteen', 'fifteen', 'seventeen', 'eighteen', 'nineteen']
        two = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        num = int(input())
        if num == 0:
            print('Zero')
        else:
            print(' '.join(numToEnghlish(num)))
except Exception:
    pass