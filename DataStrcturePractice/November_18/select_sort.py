#简单选择排序
#时间复杂度：
def select_sort(li):
	new_list = []
	for i in range(len(li)):#每遍历一遍找到一个数，所以要遍历长度遍（外层循环一趟）
		print(i)#i表示遍历几遍：遍历一遍找出一个最小值，遍历第2遍找出一个最小值，直到遍历完长度遍，才完成选择排序，共遍历列表的长度遍即6遍
		min_val = min(li)#每1遍遍历一次才可以找到最小值:O(n)，内层循环一遍
		new_list.append(min_val)
		li.remove(min_val)#删除也是:O(n)
	print(new_list)
li = [1,4,7,3,9,10,23]
select_sort(li)
print('-'*100)
#区分这两个(睡醒来分析思路）？？)
def select_sort(li):
	new_list = []
	for i in li:
		print(i)
		min_val = min(li)
		new_list.append(min_val)
		li.remove(min_val)
	print(new_list)
li = [1,4,7,3,9,10,23]
select_sort(li)
print('-'*100)
#改进后的选择排序：原地排序，不用创建新列表
# 第一层循环用来决定第一个元素的位置；
# min_index用来记录最小值的下标；
# 第二层循环用来找到和第一个元素相比，最小的那个元素，然后将min_index的下标替换成此元素的下标；
# 交换位置，将最小值不断的迭代到最前面；
def selection_sort(li):
	for i in range(len(li)-1):#i表示第几趟,外层遍历一趟：主要时要找到最小值的下标，找到有序区:指定最小值的位置
		min_dex = i
		#print(i)
		for j in range(i,len(li)):#range(a,b):表示从啊开始，到b-1结束，即不包括最后一个值bb；内层遍历：找到无序区的范围，第0趟：0~结束，第1趟：1到结束
			#print(j)
			if li[j] < li[min_dex]:
				min_dex = j
		li[i],li[min_dex] = li[min_dex],li[i]
		print(li)
li = [3,4,2,1,4,5,6,7,8,9] 
print(li)
selection_sort(li)
print('-'*100)

#我自己写的
def select_sort(li):
	for i in range(len(li)- 1):
		min_loc = i
		for j in range(i,len(li)):
			if li[j] < li[min_loc]:
				min_loc = j
		li[i],li[min_loc] = li[min_loc],li[i]
		print(li)
li = [5,6,9,2,1,4,3]
print(li)
select_sort(li)
