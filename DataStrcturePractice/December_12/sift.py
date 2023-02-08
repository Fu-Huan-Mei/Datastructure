#堆排序：python内置模块，可以直接引入使用
# import heapq
# import random
# li = list(range(100))
# random.shuffle(li)
# print(li)
# heapq.heapify(li)#建堆
# print(li)


#自己写的堆排序代码
#堆的向下调整函数，堆排序过程代码实现较难
#li表示传入的列表，low是堆的第一个元素的位置（堆顶），high是堆的最后一个元素的位置
#从父亲节点找孩子节点
def sift(li,low,high):
	#i表示堆顶位置
	i = low
	#j表示堆的左孩子节点
	j = 2 * i + 1
	#把堆顶存起来
	tmp = li[low]
	#只要j位置有数，就可以一致循环：看j位置的数上去i的位置，还是把tmp放到i的位置
	while j <= high:
		#如果有右孩子节点并且较大
		if j + 1 <= high and li[j+1] > li[j]:
			#把j指向右孩子节点
			j = j + 1
		if li[j] > tmp:
			li[i] = li[j]
			#往下看一层
			i = j
			j = 2 * i + 1
		else:
			#tmp更大，把tmp放到i的位置上
			li[i] = tmp
			break
	else:
		#把tmp放到叶子节点上
		li[i] = tmp
#大根堆排序
#1、先建立堆:堆顶数已是最大值
def heap_sort(li):
	#2、从孩子节点找父亲节点公式：(i-1) // 2=len(li)-1-1//2= length(li)-2//2=n-1-1//2
	#注意：n-1表示最后一个节点的下标（索引）
	n = len(li)
	#3、倒着遍历列表
	for i in range(n-2//2,-1,-1):
		#i表示建堆时调整部分的堆的下标，即堆顶low
		#high都指整个堆的最后一个位置
		#n-1表示整个堆的最后一个元素下标
		sift(li,i,n-1)
	# print(li)
	#2、挨个出数
	#i一直指向堆的最后一个位置
	for i in range(n-1,-1,-1):
		#让堆顶和最后一个位置做交换
		li[0],li[i] = li[i],li[0]
		#i-1表示新的high最后堆顶位置
		sift(li,0,i-1)



li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)
heap_sort(li)
print(li)




