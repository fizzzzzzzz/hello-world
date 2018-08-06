def product(*args):
    s = 1
    if not args:         #空的元组不等于None, 不能用“args == None”. 空list dict string同
        return '无'
    for n in args:
        s = s * n
    return s
    
print(product())
