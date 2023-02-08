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
#1、li表示传入的列表，first表示最小的元素（序号），last表示最大的元素（序号）
def merge_sort(li,first,last):
	#2、至少有2个元素
	if first < last:
		mid = (first + last) // 2
		#3、递归左边,左边有序
		merge_sort(li,first,mid)
		#4、递归右边，右边有序
		merge_sort(li,mid+1,last)
		#print(li[first:last+1])
		#5、左边和右边合并
		merge(li,first,mid,last)
li = list(range(6))
import random
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)


