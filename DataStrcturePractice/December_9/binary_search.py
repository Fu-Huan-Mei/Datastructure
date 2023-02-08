#二分查找:列表时从小到大排列
from cal_time import *
@cal_time
def binary_search(li,val):
	left = 0
	right = len(li) - 1
	while left <= right:#说明候选区有值
		mid = (left + right) // 2
		if li[mid] == val:
			return mid
		elif li[mid] > val:#说明候选区的左侧有val值
			right = mid - 1
		else:#说明候选区右侧有val值：li[mid] < val
			left = mid + 1
	else:
		#如果没有找到就退出循环
		return None
li = list(range(10000))
r = binary_search(li,3980)
print(r)