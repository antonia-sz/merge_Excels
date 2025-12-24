# merge_excels

一个用于批量合并文件夹内 Excel 表格的脚本。脚本会读取指定目录下所有 `.xlsx` 文件，合并为一个总表，并新增 `source_file` 列以保留来源文件名。

## 功能
- 扫描指定文件夹下的所有 `.xlsx`
- 读取每个文件的第一个工作表
- 纵向合并为一个总表
- 追加 `source_file` 列记录来源文件
- 输出合并后的 Excel 文件

## 依赖
- Python 3.8+
- pandas

安装依赖：
```bash
pip install pandas openpyxl
```

## 使用方法
1. 打开 `merge_excels.py`，修改 `FOLDER_PATH` 为你的 Excel 文件夹路径。
2. 运行脚本：
```bash
python merge_excels.py
```
3. 运行完成后，会在同一目录生成 `harbin_1763_merged.xlsx`。

## 输出说明
- 输出文件：`harbin_1763_merged.xlsx`
- 新增字段：`source_file`（来源文件名）

## 注意事项
- 当前脚本默认只读取每个 Excel 的第一个工作表。
- 若目录下没有 `.xlsx` 文件，`pandas.concat` 会报错，可自行加判断。
- 若需要合并其他格式（如 `.xls`），可扩展 `glob` 的匹配规则。

## 许可证
如需公开仓库，建议补充许可证（例如 MIT）。
