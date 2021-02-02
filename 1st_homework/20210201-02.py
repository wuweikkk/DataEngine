import numpy as np
from pandas import Series, DataFrame
persontype = np.dtype({'names':['name','Chinese','Math','English'],\
                     'formats':['U8','i','i','i']})
peoples=np.array([('张飞',68,65,30),('关羽',95,76,98),('刘备',98,86,88),\
                 ('典韦',90,88,77),('许褚',80,90,90)],dtype=persontype)
names=peoples['name']
Chineses =peoples['Chinese']
Maths = peoples['Math']
Englishs= peoples['English']

print('语文平均成绩为',np.mean(Chineses), '数学平均成绩为',np.mean(Maths),'英语平均成绩为',np.mean(Englishs))
print('语文最大成绩为',np.max(Chineses),'数学最大成绩为',np.max(Maths),'英语最大成绩为',np.max(Englishs))
print('语文最小成绩为',np.min(Chineses),'数学最小成绩为',np.min(Maths),'英语最小成绩为',np.min(Englishs))
print('语文方差为',np.var(Chineses),'数学方差为',np.var(Maths),'英语方差为',np.var(Englishs))
print('语文标准差为',np.std(Chineses),'数学方差为',np.std(Maths),'英语方差为',np.std(Englishs))

grade_sum=list(np.add(Chineses,Maths,Englishs))
data=DataFrame({'总成绩':grade_sum},index=np.array(names))
data= data.sort_values(by=['总成绩'],ascending=False)
print(data)
# s = []
# for i in zip(names,grade_sum):
#     s.extend(list(i))
# print(s) 