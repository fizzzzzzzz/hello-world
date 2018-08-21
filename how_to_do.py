def is_palindrome(n):        # 筛选出回数， 121 1234321 等
    s = str(n)
    return s == s[::-1]
    
if __name__ == '__main__':
    print(list(filter(is_palindrome, range(1000))))
