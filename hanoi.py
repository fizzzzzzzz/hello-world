'''转变思考方式，活用n-1'''
def hanoi(n, x, y, z):
	global step  #步数
	if n==1 :
		print(x, ' --> ', z)
		step += 1
	else:
		hanoi(n-1, x, z, y)  #将上面的n-1个由x->y
		print(x, ' --> ', z) #最下面的1个由x->z
		step += 1
		hanoi(n-1, y, x, z)  #将y上的n-1个由y->z
		
	
if __name__ == '__main__':
	n = int(input('请输入汉诺塔的层数:'))
	step = 0
	hanoi(n, 'X', 'Y', 'Z')
	print(step)
