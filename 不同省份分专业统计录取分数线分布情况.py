import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path = 'filtered.xlsx'
df = pd.read_excel(file_path)

df = df[['年份', '大学名称', '大学地点', '总分']]
df_filtered = df[df['大学地点'].isin(['北京', '河北', '安徽'])]

plt.figure(figsize=(10, 6))
sns.pointplot(x='大学地点', y='总分', data=df_filtered, palette='Set3')

plt.title('北京、河北、安徽大学分数线分布（柱状图）', fontsize=16)
plt.xlabel('地点', fontsize=22)
plt.ylabel('总分', fontsize=22)
plt.savefig("不同省份分专业统计录取分数线分布情况.png")
plt.show()

