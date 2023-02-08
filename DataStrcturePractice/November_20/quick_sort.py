#快速排序：思路分析：取一个元素p（第一个元素），使元素p归位；列表被p分成2部分，左边都比p小时，右边都比p打；递归完成排序。
def quick_sort(li,left,right):
	#取出第一个元素p，用变量先把p存起来，左边第一个空位空出来
	p = li[left]
	#进入循环：当left<right时，进入循环
	while left < right:
		#第1种情况：把右边的值从右边的第一个值开始与li[left]做比较后：如果比li[left]小，则把右边的值(li[right]放入左边的空格内，直到左右边的值相等时，循环停止
		while left < right and li[left] > li[right]:
			right = right - 1#往左走一步，继续循环
		#把右边的值放入（赋值）到左边的空位上，空出右边的位子
		li[left] = li[right]
		print(li,'right')
		while left < right and li[left] < li[right]:
			left = left + 1#往右走一步，继续循环
		#把左边的值放到右边的空位上
		li[right] = li[left]
		print(li,'left')
	#当left和right指针（位置）重合时：right = left，此时2者指向同一个空位，再把p放入这个空位中，说明p已归位
	li[left] = p
li = [5,7,4,6,3,1,2,9,8]
print(li)
quick_sort(li,0,len(li)-1)
print(li)


