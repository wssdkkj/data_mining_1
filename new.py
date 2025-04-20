import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.family'] = 'SimHei'

# 读取数据
df = pd.read_parquet('./merged_dataset.parquet')

# 数据概览
print(df.head())
print(df.info())
print(df.describe())

# 1. 缺失值分析 - 可视化缺失值热图
plt.figure(figsize=(12, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('缺失值热图')
plt.xlabel('特征')
plt.ylabel('样本')
plt.savefig('missing_values_heatmap.png', dpi=300)
plt.close()

# 2. 数据分布分析 - 直方图（所有数值型特征）
num_columns = df.select_dtypes(include=['int64', 'float64']).columns
for col in num_columns:
    plt.figure(figsize=(12, 6))
    sns.histplot(df[col], bins=30, kde=True)
    plt.title(f'{col} 分布直方图')
    plt.xlabel(col)
    plt.ylabel('频率')
    plt.savefig(f'{col}_distribution_histogram.png', dpi=300)
    plt.close()

# 获取所有类别特征
cat_columns = df.select_dtypes(include=['object', 'category']).columns

# 2. 数据分布分析 - 饼图（所有类别特征）
for col in cat_columns:
    plt.figure(figsize=(8, 8))
    # 计算每个类别的计数
    counts = df[col].value_counts()
    # 绘制饼图
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'{col} 的饼图')
    plt.axis('equal')  # 使饼图为圆形
    plt.savefig(f'{col}_pie_chart.png', dpi=300)  # 保存图像
    plt.close()  # 关闭当前图形

# 3. 散点图 - 年龄与收入的关系
plt.figure(figsize=(12, 6))
sns.scatterplot(x='age', y='income', data=df, alpha=0.6)
plt.title('年龄与收入之间的关系')
plt.xlabel('年龄')
plt.ylabel('收入')
plt.savefig('age_income_scatter.png', dpi=300)
plt.close()

# 散点图 - 收入与信用评分之间的关系
plt.figure(figsize=(12, 6))
sns.scatterplot(x='age', y='credit_score', data=df, alpha=0.6)
plt.title('年龄与信用评分之间的关系')
plt.xlabel('年龄')
plt.ylabel('信用评分')
plt.savefig('age_credit_score_scatter.png', dpi=300)
plt.close()

# 4. 分组条形图 - 性别与收入的关系
plt.figure(figsize=(12, 6))
sns.barplot(x='gender', y='age', data=df, estimator='mean')
plt.title('性别与年龄的关系')
plt.xlabel('性别')
plt.ylabel('平均收入')
plt.savefig('gender_age_barplot.png', dpi=300)
plt.close()

# 分组条形图 - 国家与收入的关系
plt.figure(figsize=(12, 6))
sns.barplot(x='country', y='age', data=df, estimator='mean')
plt.title('国家与年龄的关系')
plt.xlabel('国家')
plt.ylabel('平均收入')
plt.xticks(rotation=45)
plt.savefig('country_age_barplot.png', dpi=300)
plt.close()