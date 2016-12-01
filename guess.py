from random import randint

def inputnum(msg):
	'''
	sinput = input(msg)
	
	while True:
		if not sinput.isdigit():
			print('类型错误，请重新输入')
			sinput = input(msg)
		elif int(sinput) < 1 or int(sinput) > 100:
			print('数值超出1~100的范围，请重新输入')
			sinput = input(msg)
		else:
			ninput = int(sinput)
			break
		
	return ninput
	'''
	while True:
		try:
			ninput = int(input(msg))
			if ninput > 1 and ninput < 100:
				return ninput
			print('超出范围')
		except Exception as err:
			print('类型错误，请重新输入')
	
def main():
	nvalue = randint(1,100)
	ninput = inputnum('输入1~100：')
	ntotal = 1
	while(ninput != nvalue):
		if ninput < nvalue:
			print('数值太小')
	
		else:
			print('数值太大')

		ntotal += 1
		
		ninput = inputnum('输入1~100：')
		
	print('你猜对了')
	print('总次数为：', ntotal)
	
if __name__ == '__main__':
	main()
