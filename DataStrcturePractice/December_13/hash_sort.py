'''
2022-12-13
1、希尔排序:主要是把排序原理搞明白
2、
'''
#每组之间使用插入排序
def insert_sort_gap(li,gap):
	for i in range(gap,len(li)):#i表示摸到的牌的下标
		tmp = li[gap]
		j = i - gap#j指手里的牌
		while j >= 0 and li[j] > tmp:
			li[j+gap] = li[j]
			#j一直往前移动与tmp进行比较
			j -= gap
		li[j+gap] = tmp
 #希尔函数
def shell_sort(li):
	d = len(li)//2
	while d >= 1:
		insert_sort_gap(li,d)
		d //= 2
li = list(range(10))
import random
random.shuffle(li)
print('排序前：',li)
shell_sort(li)
print('排序后：',li)


