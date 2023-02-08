#练习1：给两个字符串s和t，盘点t是否为s的重新排列，是：返回tru，否：返回false  s="rat"  t="car"  r:c a r 
# def fuc(s,t):
# 	ss = list(s)
# 	tt = list(t)
# 	ss.sort()
# 	print(ss)
# 	tt.sort()
# 	print(tt)
# 	return ss == tt
# li = "rat"
# l = "car"
# r = fuc(li,l)
# print(r)	

#为什么我的方法是错误的呢？缩进错误
#注意代码缩进问题,但是缩进正确后代码是错误的
# def fun(s,t):
# 	ss = list(s)
# 	tt = list(t)
# 	for i in ss:
# 		# print(ss)
# 		for j in tt:
# 				# print(tt)
# 			if ss == tt:
# 				return True
# 			else:
# 				return False
# li = "rac"
# l = "car"
# r = fun(li,l)
# print(r)

#查找排序：给定一个m*n的二维列表，查找一个数是否存在，列表有下列特性：每一行的列表从左到右已排好顺序；每一行的第一个数比上一行的最后一个数大
#li = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
#线性查找
def sort(l,x):
	for i in l:
		#i表示一个列表
		# print(i)
		if x in i:
			return True
li = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
r = sort(li,50)
print(r)
#二分查找
def sort(l,x):
	#找到二位列表的长和宽
	#获取列标的长度，几行
	h = len(l)
	#获取列表的宽度，几列
	if h == 0:#注意这点
		return False
	w = len(l[0])
	if w == 0:#注意这点
		return False
	#初始化变量，二分查找开始运用
	left = 0
	right = h * w - 1
	while left <= right:
		mid = (left+right) // 2
		i = mid // w#难点
		j = mid % w#难点
		if l[i][j] == x:
			return True
		elif l[i][j] > x:
			#指针继续往左移动进行查找
			right = mid - 1
		else:
			#指针继续往右移动进行查找
			left = mid + 1
	else:
		return False		
li = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
r = sort(li,50)
print(r)