#2022-11-26
# cars = ['Porsche', 'BMW', 'Volvo']
# cars.sort()
# print(cars)
# #练习1：给定两个字符串s和t，判断t是否为s重新排列后组成的单词：
# #s = 'anagram',t = 'nagaram',return true;s = 'rat',t = 'car',return false
def isAnagram(s,t):
	ss = list(s)
	#print(ss)#['r', 'a', 't']
	tt = list(t)
	#print(tt)#['c', 'a', 'r']
	ss.sort()#默认情况下，sort() 方法对列表进行升序排序
	print(ss)#['a', 'r', 't']
	tt.sort()#
	print(tt)#['a', 'c', 'r']
	return ss == tt
print(isAnagram('rat','car'))

# def isAnagram(s,t):
# 	#sorted对序列（列表、元组、字典、集合、还包括字符串）进行排序
# 	return sorted(list(s)) == sorted(list(t))
# print(isAnagram('rat','car'))

#练习2：给定一个m*n的二维列表，查找一个数是否存在，列表有以下特性：
#每一行的列表从左往右已经排好序；每一行第一个数比上一行最后一个数大；
#传入任意一个数，找到就返回true。
#方式一：线性查找
# def searchMatrix(matrix,target):
# 	for line in matrix:#O(m)
# 		#print(line)
# 		if target in line:#O(n)
# 			return True
# 		return False
# li = [
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# 	]	
# print(searchMatrix(li,9))
#方式二：二分查找（未完）
# def searchMatrix(matrix,target):
# 	height = len(matrix)#列表几行
# 	#print(height)#3
# 	width = len(matrix[0])#列表几列
# 	#print(width)#3

#练习3：给定一个列表和一个整数，设计算法找到两个数的下标（与列表的长度有关），使得两个数之和为给定的整数，保证肯定仅有一个结果；
#例如：列表[1,2,5,4]与目标整数3，1+2=3，结果为[0，1]
#方式一：时间太慢了
def twoSum(nums,target):
	n = len(nums)#4（这里不是我想出来的,我没有想出来）
	for i in range(n-1):#n-1=3:i遍历序号为：0、1、2(这个是我自己想出来的，哈哈哈)
		for j in range(i+1,n):#遍历序号为：123、23、3(这个是我自己想出来的，哈哈哈)
			if nums[i] + nums[j] == target:
				return sorted([i,j])#sort()函数专门返回一个列表，这个返回一个列表
print(twoSum([1,2,5,4],3))
#方式二：
