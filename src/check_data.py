import pandas as pd

file_path = "data/raw/International sale Report.csv"

df = pd.read_csv(file_path)

print("=== 基本資訊 ===")
print(f"資料筆數：{len(df):,}")
print(f"欄位數：{len(df.columns)}")

print("\n=== 欄位 ===")
print(df.columns.tolist())

print("\n=== 缺失值 ===")
print(df.isna().sum())

print("\n=== Customer 數量 ===")
print(f"不同 Customer：{df['CUSTOMER'].nunique():,}")

print("\n=== 重複資料 ===")
print(f"完全重複的 rows：{df.duplicated().sum():,}")

print("\n=== 日期 ===")
print(df["DATE"].min())
print(df["DATE"].max())

print("\n=== Customer 前 10 名 ===")
print(df["CUSTOMER"].value_counts().head(10))

print("\n=== Customer 看起來像月份的資料 ===")

month_pattern = r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{2}$"

suspicious_customer = df[
    df["CUSTOMER"].astype(str).str.match(month_pattern, na=False)
]

print(suspicious_customer.head(20))

print("\n異常筆數：")
print(len(suspicious_customer))

print("\n=== 欄位錯位發生前後 ===")

print(df.iloc[19670:19682].to_string(index=False))

print("\n=== 第一個資料表結尾 ===")
print(df.iloc[19660:19675].to_string(index=False))
print("\n=== 第二個資料表大小 ===")

second_table = df.iloc[19676:]

print(f"第二個資料表 rows：{len(second_table):,}")
print(second_table.tail().to_string(index=False))
print("\n=== 第一個表格尾端：更多資料 ===")
print(df.iloc[19450:19600].to_string(index=False))
