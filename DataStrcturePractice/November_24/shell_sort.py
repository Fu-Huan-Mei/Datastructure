#2022-11-24
#记住这一点：i就是手机的牌，j就是摸到的牌
#每组用插入排序：全部组同时排序
#（表示分的组）gap=d（表示分组的间隔)
# def insert_sort_gap(li,gap):
# 	for i in range(gap,len(li)):#i表示摸到牌的下标
# 		variable = li[i]
# 		j = i - gap#j表示手里牌的下标
# 		#当手里右派并且手里的牌比摸到的牌的值大时
# 		while j >= 0 and li[j] > variable:
# 			#就把手里的牌往后移动
# 			li[j+gap] = li[j]
# 			#此时再把手里的牌和前一张牌作比较
# 			j = j - gap
# 		li[j+gap] = variable


# #希尔排序的代码实现
# def shell_sort(li):
# 	d = len(li) // 2#d表示列表元素的下标
# 	while d >= 1:#当d=1时，列表就排好序了；所以当d<=1时，列表就还在插入排序
# 		insert_sort_gap(li,d)
# 		d = d //2
# 	#while循环结束以后，就说明已排好顺序

# li = list(range(10))
# import random
# random.shuffle(li)
# shell_sort(li)
# print(li)

#计数排序
#from cal_time import *

#@cal_time

def count_sort(li,max_count=100):
	count = [0 for _ in range(max_count+1)]
	for val in li:#val表示遍历列表的值
		count[val] += 1#我们创建的count列表的序号与值相同
	#清空原列表li，准备放入排好序的元素
	li.clear()
	#此时遍历count列表的序号和值
	for ind,val in enumerate(count):
		for i in range(val):
			li.append(ind)
#@cal_time
def sys_sort(li):
	li.sort()

import random 
li = [random.randint(0,100) for _ in range(20)]
print(li)
count_sort(li)
print(li)

#li1 = copy.deepcopy(li)
#li2 = copy.deepcopy(li)

#count_sort(li1)
#sys_sort(li2)


'''
#1、已知列表的范围 
li = [1,3,2,4,1,2,3,1,3,5]
#2、计数范围count
count的值value:0,1,2,3,4,5
根据列表li来计算count的value出现的次数index：0，3，2，3，1，1
'''

