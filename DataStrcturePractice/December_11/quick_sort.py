'''
2022-12-11
1、快速排序：递归思想:可以跟着老师思路去思考明白这个问题，但是还不能独立写出代码
'''

#分区函数
import random

def partition(li,left,right):
	tmp = li[left]
	while left < right:
		while li[right] >= tmp and left < right:#从右边比tmp小的值（数）
			#right左移
			right = right - 1
			#把右边的值写到左边的空位上
		li[left] = li[right]
		# print('左边归位：',li)
		while li[left] <= tmp and left < right:
			#left往右移动
			left = left + 1
			#把左边的值写到右边的空位上
		li[right] = li[left]
		# print('右边归位：',li)
	li[left] = tmp#把tmp归位
	return left#或者right也OK,因为最后left和right都碰到一起了,该位置就是tmp=5的位置即中间mid位置
# li = [5,7,4,6,3,1,2,9,8]
# print('归位前：',li)
# partition(li,0,len(li)-1)
# print('归位后：',li)#归为后的结果应该是：左边的数都比tmp小，右边的数都比tmp大
from cal_time import *
#注意：不能把装饰器放到递归函数前
#快排函数：O(nlogn) logn层，每一层时间复杂度是n
def _quick_sort(li,left,right):
	if left < right:#至少有两个元素（递归条件）
		mid = partition(li,left,right)#调用分区函数以后说明第一个元素：5已经完成归位，然后由5这个元素把列表分成两部分：左边都是比5小的数，右边都是比5大的数
		_quick_sort(li,left,mid-1)#递归：快速排序：左边
		_quick_sort(li,mid+1,right)#递归：快速排序：右边
@cal_time
def quick_sort(li):
	_quick_sort(li,0,len(li)-1)
li = list(range(100))
random.shuffle(li)
print('归位前：',li)
quick_sort(li)
print('归位后：',li)
