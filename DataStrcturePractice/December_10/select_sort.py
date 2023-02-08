'''
常见排序算法
1、low：冒泡排序、选择排序、插入排序
2、NB：快速排序、堆排序、归并排序
3、其他：希尔排序、计数排序、基数排序
'''
#选择排序:每遍历一趟找一个最小的数
# def select_sort_simple(li):
# 	#装进排好序的值
# 	new_li = []
# 	#共遍历len(li)趟
# 	for i in range(len(li)):
# 		#每遍历一趟在列表种找出一个最小值
# 		min_val = min(li)#O(n)
# 		#把最小值添加到新列表里
# 		new_li.append(min_val)
# 		#同时，删除原列表的最小值
# 		li.remove(min_val)#O(n)
# 	return new_li
# li = [3,7,9,1,10,23,90]
# print('排序前=',li)
# r = select_sort_simple(li)
# print('排序后=',r)
#上述排序问题：时间复杂度为O(n^2)，即运行效率叫低；而且新列表也占内存

#改进后的选择排序:找到第一个最小的数的位置与列表的第一个位置交换
# def select_sort(li):
# 	for i in range(len(li)-1):#i表示第几趟，最后一趟无需遍历，已经默认排好顺序
# 		min_loc = i
# 		#无序区范围:第0趟：从0到最后；第1趟：从1到最后；第i趟，从i到最后
# 		#无序区的range()函数：前包后不包
# 		#i+1表示自身数字之间不比较
# 		for j in range(i+1,len(li)):
# 			if li[j] < li[min_loc]:
# 				min_loc = j
# 			li[i],li[min_loc] = li[min_loc],li[i]
# 		print(f'第{i}趟排序后:',li)

# li = [3,7,9,1,10,23,90]
# print('排序前=',li)
# select_sort(li)



