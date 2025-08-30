import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

file_path = 'filtered.xlsx'
df = pd.read_excel(file_path)
df = df[['大学标签', '总分']]

def categorize_university(tag):
    if not isinstance(tag, str):
        tag = str(tag)
    if re.search(r'985', tag):
        return '985高校'
    elif re.search(r'211', tag):
        return '211高校'
    elif re.search(r'双一流', tag):
        return '双一流高校'
    else:
        return '其他高校'

plt.figure(figsize=(10, 6))
sns.boxplot(x='大学类型', y='总分', data=df, palette='Set3')

plt.title('不同大学类型的分数分布', fontsize=16)
plt.xlabel('大学类型', fontsize=12)
plt.ylabel('总分', fontsize=12)

plt.show()