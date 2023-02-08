#2022-11-23
#1、topk问题：小根堆问题(不理解？？？)
#2、堆排序：大根堆排序(比较排序)
#代码实现：
#1、向下调整的函数
# def sift(li,top,last):
# 	i = top
# 	j = 2 * i + 1
# 	variable = li[top]
# 	while j <= last:
# 		if j+1 <= last and li[j+1] < li[j]:
# 			j = j + 1
# 		if li[j] < variable:
# 			li[i] = li[j]
# 			i = j
# 			j = 2 * i + 1
# 		else:
# 			break
# 		li[i] = variable
# #2、topk问题的代码实现
# def topk(li,k):
# 	heap = li[0:k]
# 	#(1)取出列表的前k个数，建堆
# 	for i in range((k-2)//2,-1,-1):
# 		sift(heap,i,k-1)
# 	#(2)遍历列表所有元素：如果比对堆顶大，就加进去，进行调整
# 	for i in range(k,len(li)-1):
# 		if li[i] > heap[0]:
# 			heap[0] = li[i]
# 			sift(heap,0,k-1)
# 			#(3)挨个出数
# 	for i in range(k-1,-1,-1):
# 		heap[0],heap[i]=heap[i],heap[0]
# 		sift(heap,0,i-1)
# 	return heap
# import random
# li = list(range(100))
# random.shuffle(li)
# print(topk(li,10))

#归并排序：代码实现（递归）
#归并：代码实现:一次归并的特性：假设列表2边都有序
def merge(li,first,mid,last):
 	i = first#第一个箭头
 	j = mid + 1#第二个箭头
 	#建立一个临时列表，装入已经排好序的元素
 	lvariable = []
	#只要左右两边都有数，那就比较两边的数的大小
 	while i <= mid and j <= last:
 		if li[i] < li[j]:
 			lvariable.append(li[i])
 			i = i + 1
 		else:
 			lvariable.append(li[j])
 			j = j + 1
 	#while执行完，肯定有一边没有数了
 	#情况一：如果左边部分有数,右边没数
 	while i <= mid:
 		lvariable.append(li[i])
 		i = i + 1
 	#情况而：如果右边部分有数，左边没数
 	while j <= last:
 		lvariable.append(li[j])
 		j = j + 1
 	li[first:last+1] = lvariable
#注意：传入的应该是列表的序号
# li = [2,5,7,8,9,1,3,4,6]
# merge(li,0,4,8)
# print(li)
#归并排序（递归）
#1、li表示传入的列表，first表示最小的元素（序号），last表示最大的元素（序号）
def merge_sort(li,first,last):
	#2、至少有2个元素，递归
	if first < last:
		mid = (first + last) // 2
		#3、递归左边,左边有序
		merge_sort(li,first,mid)
		print('左边有序',li)
		#4、递归右边，右边有序
		merge_sort(li,mid+1,last)
		print('右边有序',li)
		#5、左边和右边归并
		merge(li,first,mid,last)
		print('归并完成',li)
li = list(range(10))
import random
random.shuffle(li)
print(li)#无序列表
merge_sort(li,0,len(li)-1)
print(li)#有序列表


