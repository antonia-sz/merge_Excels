'''
脚本功能说明：读取文件夹里所有Excel，合并为一张新的总表
'''

import pandas as pd
import glob
import os

# 1. 修改为你存放 6 个 Excel 的文件夹路径
FOLDER_PATH = r"文件路径"  # ← 这里换成你的实际路径

# 2. 读取该文件夹下所有 .xlsx 文件
excel_files = glob.glob(os.path.join(FOLDER_PATH, "*.xlsx"))

print("找到的文件：")
for f in excel_files:
    print(" -", os.path.basename(f))

all_dfs = []

for file in excel_files:
    # 3. 读取每一个 Excel，默认读第一个 Sheet
    df = pd.read_excel(file)
    
    # 可选：保留来源信息，方便以后排查（哪条来自哪一个时间段文件）
    df["source_file"] = os.path.basename(file)
    
    all_dfs.append(df)

# 4. 纵向合并所有 DataFrame
merged_df = pd.concat(all_dfs, ignore_index=True)

print(f"\n合并后总行数：{len(merged_df)}")

# 5. 输出为新的总表
output_path = os.path.join(FOLDER_PATH, "harbin_1763_merged.xlsx")
merged_df.to_excel(output_path, index=False)

print(f"已保存到：{output_path}")
