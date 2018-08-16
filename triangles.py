'''
杨辉三角
          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
'''

def triangles(r):
    n = 0
    N = [1]
    while n<r:
        yield N
        N = [1] + [N[i] + N[i+1] for i in range(len(N)-1)] + [1]
        n += 1
    return 'done'
    
for i in triangles(10):
    print(i)
