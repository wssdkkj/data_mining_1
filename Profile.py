import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
from matplotlib import rcParams

# 指定字体路径
font_path = './.venv/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf'  # 根据实际路径修改
font_prop = fm.FontProperties(fname=font_path)

rcParams['font.family'] = 'SimHei'
rcParams['font.sans-serif'] = ['SimHei']

def User_Profile(data):
    # 用户画像建立
    start_time = time.time()

    # 绘制小提琴图
    plt.figure(figsize=(16, 6))

    # 小提琴图：年龄与性别
    plt.subplot(1, 2, 1)
    sns.violinplot(x='gender', y='age', data=data)
    plt.title('Violin Plot of Age by Gender')
    plt.xlabel('Gender',fontproperties=font_prop)
    plt.ylabel('Age')

    # 小提琴图：收入与性别
    plt.subplot(1, 2, 2)
    sns.violinplot(x='gender', y='income', data=data)
    plt.title('Violin Plot of Income by Gender')
    plt.xlabel('Gender',fontproperties=font_prop)
    plt.ylabel('Income')

    plt.tight_layout()
    plt.savefig('./figures/violin_gender_30.png', dpi=300)
    plt.close()

    print('Gender Violin plots finished.')

    # 绘制小提琴图：年龄与国家
    plt.figure(figsize=(16, 12))

    plt.subplot(2, 1, 1)
    sns.violinplot(x='country', y='age', data=data)
    plt.title('Violin Plot of Age by Country')
    plt.xlabel('Country',fontproperties=font_prop)
    plt.ylabel('Age')

    # 小提琴图：收入与国家
    plt.subplot(2, 1, 2)
    sns.violinplot(x='country', y='income', data=data)
    plt.title('Violin Plot of Income by Country')
    plt.xlabel('Country',fontproperties=font_prop)
    plt.ylabel('Income')

    plt.tight_layout()
    plt.savefig('./figures/violin_country_30.png', dpi=300)
    plt.close()

    print('Country Violin plots finished.')

    end_time = time.time()
    elapsed_time = end_time - start_time  # 计算运行时间
    print(f'Profile time: {elapsed_time:.2f} seconds')  # 打印运行时间

if __name__ == '__main__':
    data = pd.read_parquet('./data_clean_30.parquet')
    print('User profile begins.')
    User_Profile(data)