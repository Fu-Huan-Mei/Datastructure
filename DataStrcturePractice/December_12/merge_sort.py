
#归并排序:假设列表分两段有序，如何合并为一个有序列表？？
#时间复杂度：O(n(logn))
#空间复杂度:O(n)
#归并函数
def merge(li,low,mid,high):
	i = low
	j = mid + 1
	li_tmp = []
	#只要左右两边都有数
	while i <= mid and j <= high:
		if li[i] < li[j]:
			li_tmp.append(li[i])
			#把i后移
			i += 1
		else:
			li_tmp.append(li[j])
			#把j后移
			j += 1
	#while循环执行完以后，肯定有一部分已经没有数字了
	#如果左边部分有数
	while i <= mid:
		li_tmp.append(li[i])
		i += 1
	#如果右边部分有数
	while j <= high:
		li_tmp.append(li[j])
		j += 1
		#li从low到high截取的范围
	li[low:high+1] = li_tmp


#递归思想
#分解：将列表越分越小，直至分成一个元素
#（终止条件）终止条件：一个元素是有序的
#合并：将两个有序列表归并，列表越来越大
#假如列表两边无序,下列函数将会使列表有序
def merge_sort(li,low,high):
	if low < high:#至少有两个元素
		mid = (low + high) // 2
		#先递归左边排好序(不怎么理解？？)
		merge_sort(li,low,mid)
		#再递归右边（不怎么理解？？）
		merge_sort(li,mid+1,high)
		#左右两边归并
		merge(li,low,mid,high)
li = list(range(10))
import random
random.shuffle(li)
print('排序前:',li)
merge_sort(li,0,len(li)-1)
print('排序后:',li)