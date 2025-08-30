import pandas as pd

# 读取Excel文件
file_path = 'data.xlsx'  # 请替换成你的文件路径
df = pd.read_excel(file_path)

# 查看数据的前几行，确保列名正确
print(df.head())

# 设置各类专业及其可以报考的研究生专业规则
admission_rules = {
    '数学': ['数据科学', '统计学', '运筹学', '计算数学', '应用数学', '金融数学', '精算学'],
    '计算机': ['计算机科学与技术', '软件工程', '网络工程', '人工智能', '信息安全', '大数据', '云计算','电子与通信工程', '电气工程', '控制工程', '自动化', '嵌入式系统'],
}

# 筛选符合条件的本科专业和可以报考的研究生专业
filtered_df = pd.DataFrame()

# 遍历所有的规则，筛选出符合条件的行
for undergrad_major, grad_programs in admission_rules.items():
    filtered_df = pd.concat([filtered_df, df[
        df['专业类型'].str.contains(undergrad_major, case=False, na=False) 
    ]])


# 筛选符合条件的数据
filtered_df = pd.DataFrame()

# 遍历所有的规则，筛选出符合条件的行
for undergrad_major, grad_programs in admission_rules.items():
    filtered_df = pd.concat([filtered_df, df[
        df['专业类型'].str.contains(undergrad_major, case=False, na=False) 
    ]])

# 保留符合条件的行，删除不符合条件的行
final_df = filtered_df.copy()

# 如果需要，将筛选后的数据保存到新的Excel文件
final_df.to_excel('filtered_data_with_matching_rows_only.xlsx', index=False)

# 查看筛选后的结果
print(final_df)