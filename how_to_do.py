def is_palindrome(n):        # 筛选出回数， 121 1234321 等
    s = str(n)
    return s == s[::-1]

def by_score(t):             #元组排序方法
    return -t[1]
    
if __name__ == '__main__':
    print(list(filter(is_palindrome, range(1000))))
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    L_score = sorted(L, key=by_score)
