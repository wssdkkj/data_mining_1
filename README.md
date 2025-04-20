# 代码使用说明
代码仓库下载完成后，代码有整体运行与模块化运行两种方式。

## 整体运行
在终端中运行：
```Python
python main.py
```
注：整体运行未经过完全测试，谨慎使用。

## 模块化运行
### 加载数据
确保数据集路径正确，可通过修改代码段
```df = load_data('./30G_data_new')```
来改变数据集路径。

然后在终端中运行```python LoadData.py```，会打印数据集基本信息与耗时，
运行结束后会生成`output_data_x.parquet`文件，可通过修改代码段
```output_file = './output_data_30.parquet'```
进行修改。

## 探索性分析
模块化运行下，探索性分析将读取中间文件`output_data_x.parquet`，对应代码段为
```data = pd.read_parquet('./output_data_30.parquet')```

在终端中运行```python EDA.py```，会打印该部分用时，运行结束后将生成对应可视化图像，保存在`figures`文件夹下。

## 数据预处理
预处理部分同样读取中间文件`output_data_x.parquet`。

在终端中运行
```python preprocess.py```
将打印缺失值与异常值的统计，并给出处理前后的数据集行数以及所用处理时间，并生成处理后的数据文件`data_clean_x.parquet`，通过修改代码段```output_file = './data_clean_30.parquet'```来修改输出路径。

## 用户画像建立
模块化方式中将读取中间文件`data_clean_x.parquet`，在终端中运行
```python preprocess.py```
将打印所用时间，并在`figures`文件夹下生成对应可视化结果。
