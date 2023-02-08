#查找
#1、顺序查找:linear_search:从头到尾查找
def func(list,value):
	for n,number in enumerate(list,start = 0):#因为要返回下标，所以n和number都需要（重点）
		if number == value:#if是单个分支
			return n
	else:#for和else才是在一起运行的，else表示for正常运行继续执行else（重点）
		return None
list = [1,2,3,4,5]
print(func(list,5))#这个语句没有写出来

# enumerate() 方法
#seasons = ['Spring', 'Summer', 'Fall', 'Winter']
#print(list(enumerate(seasons)))
#print('-'*60)

#seq = ['one','two','three']
#for i,number in enumerate(seq):
	#print (i,number)
#print('-'*60)

#i = 0#做了这步
#seq =  ['one', 'two', 'three']
#for number in seq:
#	print(i,number)#多了这步
#	i += 1

'''
这种就是我自己的写法和想法，解决了我的困惑
1、为什么顺序查找要返回数组下标？洗澡我自己想了一下：
如果不返回下标，就只能返回查找到的值，或者返回True，但是这样的话我们就与原来的数组没有了什么联系。
'''
def linear_search(value):
	for num in range(0,5):
		if num == value:
			return True
	else:
		print(None)

#print(linear_search(3))
linear_search(5)





