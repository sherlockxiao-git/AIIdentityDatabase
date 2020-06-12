import numpy as np
array1=np.zeros((2,4))
# array4=np.full()
array5=np.eye(3,3)#不使用元组
array2=np.array([1,2,4]) #([[]])
array3=np.empty((2,5))

array6=np.linspace(0,10,num=5)

array7=np.random.random(3,3)#随机生成3*3 [0,1)范围的数
array8=np.random.normal(0,1,(2,2))#均值0,方差1
array9=np.random.permutation()#重新排序数组  .shuffle() 在原来的基础上修改
array10=np.random.choice(array1,size=(3,4))#随机抽样,独立抽样


# print(array1)
# print(array1.shape)
# print(array3)
# print(array3.dtype)
print(array6)