#插入排序：有点儿插不清楚？？？
def insert_sort(li):
	for i in range(1,len(li)):#要摸到的牌（桌子上的）:无序区
		insert_value = li[i]#摸到一张牌:插入值,提前进行保存
		j = i - 1#已有一张牌（手里的):记录插入的下标（位置），j+1表示插入的位置：有序区
		while j >= 0 and li[j] > insert_value:#不用for循环是因为j为-1的情况,因为循环有条件
			li[j+1] = li[j]#结果：li = [10,10,9,8,1,2,4]，6保存在insert_value这个临时变量里
			j = j - 1#再让insert_value与前一个数进行比较：如果j<0，就退出循环
		li[j+1] = insert_value
		print(li)
li = [10 ,6,9,8,1,2,4]
print(li)
insert_sort(li)                          
print('-'*100)
#我自己理解后写出来：想着实例才好写
def insert_sort(li):
	#确认无序区的值，即桌上的牌
	for i in range(1,len(li)):
		#先保存在一个临时变量里
		insert_value = li[i]
		#j确认有序区的位置（下标），即手中的牌
		j = i - 1
#当手中牌的位置>=0并且手中的牌>插入的值时：才进入循环：先把0和12个位置的数值进行比较，再把的值较大的数移到后一个位置
		while j >= 0 and li[j] > insert_value:
#只讲序列的第一二两个做实例：当6（插入值）和10（手中值）比较后：需要把10后移一个位置
#把手中的牌后移一个位置：有些同学会担心该值会把插入值覆盖，但是我们已经提前设置临时变量来保存该插入值了：insert_value
			li[j+1] = li[j]#运行结果：li = [ ,10,9,8,1,2,4] insert_value = [6]
			#j = 0,j+1=1,再把插入值往前移一个进行比较，则此时位置:j=j-1
			j = j - 1
			#当j<0时就退出循环:说明手里已经没有牌了；把待插入的值与手中的值交换，此时j=-1
		li[j+1] = insert_value
		print(li)
li = [10 ,6,9,8,1,2,4]
print(li)
insert_sort(li)   

