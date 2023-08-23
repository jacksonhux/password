password = '10'
x = 0
while True :
	ans = input('請輸入密碼:')
	x = x+1
	y = 3-x
	if ans == password and x <3 :
		print('pass')
		break
	elif x <3 :
		print('failto login,you have' ,y,'chance')
	else:
		print('fail to attemt')
		break


