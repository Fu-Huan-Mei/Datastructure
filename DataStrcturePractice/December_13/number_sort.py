# 计数排序  ？？不懂这些列表为谁创建
def count_sort(li,max_count = 10):
	#建立一个计数列表
	count = [0 for _ in range(max_count+1)]
	for val in li:
		count[val] = count[val] + 1
	li.clear()
	for ind,val in enumerate(count):
		for i in range(val):
			li.append(ind)
import random
li = [random.randint(0,10) for _ in range(100)]
print('排序前：',li)
count_sort(li)
print('排序后：',li)
