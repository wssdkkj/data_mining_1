import pandas as pd
import time

def preprocess(data):
    # 数据预处理
    start_time = time.time()

    # 统计缺失值和异常值
    missing_info = data.isnull().sum()
    missing_percentage = (missing_info / len(data)) * 100
    missing_info_df = pd.DataFrame({'Missing Values': missing_info, 'Percentage': missing_percentage})

    # 统计异常值数量
    outlier_info = {}
    for column in ['age', 'income']:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        outlier_condition = (data[column] < (Q1 - 1.5 * IQR)) | (data[column] > (Q3 + 1.5 * IQR))
        outlier_count = outlier_condition.sum()
        outlier_info[column] = outlier_count

    # 打印统计信息
    print(f"Data rows before handling: {len(data)}")
    print("Missing values count and percentage:")
    print(missing_info_df[missing_info_df['Missing Values'] > 0])
    print("Outlier counts:")
    print(outlier_info)

    # b. 缺失值处理
    # 对数值特征用均值填充
    for column in ['age', 'income']:
        mean_value = data[column].mean()
        data[column] = data[column].fillna(mean_value)

    # 对类别特征删除含有缺失值的行
    data = data.dropna(subset=['gender', 'country'])
    print(f"Data rows after missing value handling: {len(data)}")

    # c. 处理异常值（假设阈值为1.5倍IQR）
    for column in ['income', 'age']:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        outlier_condition = (data[column] < (Q1 - 1.5 * IQR)) | (data[column] > (Q3 + 1.5 * IQR))
        data = data[~outlier_condition]

    print(f"Data rows after outlier removal: {len(data)}")

    end_time = time.time()
    elapsed_time = end_time - start_time  # 计算运行时间
    print(f'preprocess time: {elapsed_time:.2f} seconds')  # 打印运行时间

    return data

if __name__ == '__main__':
    data = pd.read_parquet('./output_data.parquet')
    print('preprocess begins.')
    new_data = preprocess(data)
    output_file = './data_clean_30.parquet'
    new_data.to_parquet(output_file, index=False)
    print(f'DataFrame 已保存为 {output_file}')