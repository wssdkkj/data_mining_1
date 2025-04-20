import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
from matplotlib import rcParams
import pandas as pd
import time

# 指定字体路径
font_path = './.venv/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf'  # 根据实际路径修改
font_prop = fm.FontProperties(fname=font_path)

rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']

def eda(data):
    start_time = time.time()

    # 数值特征——直方图
    plt.figure(figsize=(25, 12))

    plt.subplot(1, 2, 1)
    sns.histplot(data['age'], bins=20, kde=False)
    plt.title('Initial Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')

    plt.subplot(1, 2, 2)
    sns.histplot(data['income'], bins=20, kde=False)
    plt.title('Initial Income Distribution')
    plt.xlabel('Income')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.savefig('./figures/histogram_30.png', dpi=300)
    plt.close()

    print('Histogram Plot Finished.')

    # 类别特征——饼图
    plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    gender_counts = data['gender'].value_counts()
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90,
            textprops={'fontproperties': font_prop})
    plt.title('Initial Gender Distribution')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    country_counts = data['country'].value_counts()
    plt.pie(country_counts, labels=country_counts.index, autopct='%1.1f%%', startangle=90,
            textprops={'fontproperties': font_prop})
    plt.title('Initial Top 10 Countries Distribution')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('./figures/pie_30.png', dpi=300)
    plt.close()

    print('Pie Plot Finished.')

    # 数值特征关系——散点图
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=data, x='age', y='income',marker='o',s=10)
    plt.legend([])  # 禁用图例
    plt.grid(False)  # 禁用网格线
    plt.title('Income vs Age')
    plt.savefig('./figures/scatter_30.png', dpi=300)
    plt.close()

    print('Scatter Plot Finished.')

    end_time = time.time()
    elapsed_time = end_time - start_time  # 计算运行时间
    print(f'EDA time: {elapsed_time:.2f} seconds')  # 打印运行时间

if __name__ == '__main__':
    data = pd.read_parquet('./output_data_30.parquet')
    print('EDA begins.')
    eda(data)