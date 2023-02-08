#汉诺塔问题：递归实现（重点理解）
def hanoi(n,a,b,c):
	if n == 1:
		#基线条件
		print("从%s移动到%s"%(a,c))
	else:
		#递归条件
		hanoi(n-1,a,c,b)
		print("从%s移动到%s"%(a,c))
		hanoi(n-1,b,a,c)
hanoi(3,'A','B','C')