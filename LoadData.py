import pandas as pd
import os
import time

def load_data(folder_path):
    start_time = time.time()

    dataframes = []
    parquet_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.parquet')]
    for file in parquet_files:
        print('Loading {}'.format(file))
        part = pd.read_parquet(file,engine='fastparquet',columns=['age','income','gender','country'])
        dataframes.append(part)
        del part
    df = pd.concat(dataframes, ignore_index=True)

    end_time = time.time()  # 记录结束时间
    elapsed_time = end_time - start_time  # 计算运行时间
    print(f'Load data time: {elapsed_time:.2f} seconds')  # 打印运行时间

    print(df.info())
    print(df.describe())

    return df

if __name__ == '__main__':
    df = load_data('./30G_data_new')
    output_file = './output_data_30.parquet'
    df.to_parquet(output_file, index=False)
    print(f'DataFrame 已保存为 {output_file}')