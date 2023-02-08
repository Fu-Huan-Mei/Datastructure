#二分查找：选默特的示例
#1、先创建一个函数：传入待查找的列表和要找到的值
#2、left和right分别表示列表的索引值：第一个和最后一个
#3、进入循环：只要候选区就说明还有有值，就要一直循环:找到列表中间值，与value对比之后；再去找中间值，再与value对比之后；直到找到value为止 
#4、mid表示中间值的索引
#5、把中间值new_list[mid]和value作比较
#6、终于找出来那里有问题了：我的（left + right)没有打括号
def binary_search(new_list,value):
	left = 0                      
	right = len(new_list) - 1
	while left <= right:
		mid = (left + right) // 2 #不要忘记写括号了！！！！！！
		if new_list[mid] == value:
			return mid
		elif new_list[mid] > value:
			 right = mid - 1
		else:
			left = mid + 1
	else:
		return None
li = list(range(1,6))
print(binary_search(li,6))

li = [1,2,3,4,5]
print(binary_search(li,5))


