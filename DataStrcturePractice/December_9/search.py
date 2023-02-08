'''
2022-12-9
'''


#顺序查找
#参数:l表示列表，n表示要查找的值
from cal_time import *
@cal_time
def search(l,n):
	#i表示列表l值的索引
	for i in range(len(li)-1):
		if li[i] == n:
			return i
	#注意return None的位置，列表全部遍历结束以后才可以得出结论：找到或找不到
	return None
li = list(range(10000))
r = search(li,3980)
print(r)







	


