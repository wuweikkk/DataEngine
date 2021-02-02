
import pandas as pd
# 数据加载
df=pd.read_csv(r'car_complain.csv')
# 数据预处理
df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
# 数据清洗
df['brand']=df['brand'].replace('一汽-大众','一汽大众')
df['brand']=df['brand'].replace('一汽-大众奥迪','一汽大众奥迪')

# 按照brand统计问题总数
result=df.groupby(['brand'])['id'].agg(['count'])
# tags=df.columns[7:]
# result2=df.groupby(['brand'])[tags].agg('sum')
# 问题总数排序
# result2=result.merge(result2,left_index=True,right_index=True,how='left')
# result2.reset_index(inplace=True)
# 按照count从大到小排序
result=result.sort_values(by=['count'],ascending=False)
print(result)

#按照车型统计问题总数
result2=df.groupby(['car_model'])['id'].agg(['count'])
result2=result2.sort_values(by=['count'],ascending=False)
print(result2)

#车型品牌平均投诉
result3=df.groupby(['brand','car_model'])['id'].agg(['count']).groupby('brand').mean()
result3=result3.sort_values(by=['count'],ascending=False)
print(result3)
