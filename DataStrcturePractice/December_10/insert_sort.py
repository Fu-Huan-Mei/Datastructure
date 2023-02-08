'''
插入排序：将整个数组 nums 分为有序和无序的两个部分。前者在左边，后者在右边。
最开始有序的部分只有第一个元素，其余都属于无序的部分。每次取出无序部分的第一个(最左边)元素，把它加入有序部分。
通过比较找到属于该元素的位置 k，然后将原 k 位置及其后面的有序部分元素都向右移动一个位置，
有序的部分即增加了一个元素，无序部分减少了一个元素。这样一直继续下去，直到无序的部分没有元素，整个插入排序就算完成。
'''
# def insert_sort(li):
# 	#i表示摸到牌的下标
# 	for i in range(1,len(li)):
# 		#用变量存起来手里摸到的牌
# 		tmp = li[i]
# 		#i- 1:i的前一张牌的下标，即手里的牌；刚开始为手里最后一张牌:j i (li[j] tmp)
# 		j = i - 1
# 		#当j=-1时退出
# 		#找插入的位置
# #当手里的牌大于要插入的那张牌时，就把手里这张牌后移，再把要插入的牌（tmp)继续和前一张牌(li[j])作比较
# 		while li[j] > tmp and j >= 0:
# 			#把较大这张牌往后移
# 			li[j+1] = li[j]
# 			#把j的箭头往左移再进行比较，直到j=-1时，才停止，因为j=-1代表已经和手里的牌全部比较完了
# 			j = j - 1
# 		#循环结束就表示已经找到要插入牌的位置了
# 		li[j+1] = tmp
# 		print(li)
# li = [3,1,2,9,5,0,4]
# insert_sort(li)



#插入排序
def insert_sort:
	#1、找牌：找到要插入的牌的索引i
	for i in range(len(li)):
		#用一个变量存起来，因为要单独和手里的牌来作比较
		tmp = li[i]
		#j表示手里拍的下标（索引）
		j = i - 1
		#2、找到牌后与手里的牌作比较后，找到和合适的位置把牌插进去
		#当j>=0时，说明手里有牌；当li[j] > tmp时，
		while j >= 0 and li[j] > tmp:
			#把手里牌后移
			li[j+1] = li[j]
			#把摸到的牌的序号继续往前移动，与手里其他牌做比较
			j = j - 1
		#当循环结束时，就找到了tmp牌的位置了
		li[j+1] = tmp
		print(li)
li = [3,1,2,9,5,0,4]
insert_sort(li)


