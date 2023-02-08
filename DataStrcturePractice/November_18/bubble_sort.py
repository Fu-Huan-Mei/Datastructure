#冒泡排序（bubble_sort)
#第一种
def bubble_sort(li):
	for i in range(len(li)-1):#i表示第几趟，i是从0开始计算的；外层循环一趟,内层要循环len(li)-i-1次（因为最后依次的内层循环已经排好序了）
		for j in range(len(li)-i-1):#内层循环
			if li[j] > li[j+1]:#自己写时忘记交换值了，还有就是看图来理解就更好理解了
				li[j],li[j+1] = li[j+1],li[j]
		print(li)
li = [1,2,3,4,5]
bubble_sort(li)
print('-'*60)
#运行结果如下：
#第0趟：[1,2,3,4,5]
#第1趟：[1,2,3,4,5]
#第2趟：[1,2,3,4,5]
#第3趟：[1,2,3,4,5]
#第4趟：[1,2,3,4,5]
None

#改进后：从以上代码运行结果可以发现：第3趟语句排好序了，但是第4趟还要循环1次，所以想改进的点：当内层循环的数字不发生交换时，就停止循环
def bubble_sort(li):
	for i in range(len(li)-1):#i表示第几趟，i是从0开始计算的；外层循环一趟,内层要循环len(li)-i-1次（因为最后依次的内层循环已经排好序了）
		exchange = False#不怎么懂为什么要加在这里？？
		for j in range(len(li)-i-1):#内层循环
			if li[j] > li[j+1]:#自己写时忘记交换值了，还有就是看图来理解就更好理解了
				li[j],li[j+1] = li[j+1],li[j]
				exchange = True
		print(li)
		if not exchange:
			return
li = [1,2,3,4,5]
bubble_sort(li)
