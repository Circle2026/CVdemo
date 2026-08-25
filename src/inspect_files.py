from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw")


for file in RAW_DIR.glob("*.csv"):
    print("\n" + "=" * 70)
    print(f"檔案：{file.name}")

    try:
        df = pd.read_csv(file)

        print(f"資料大小：{df.shape}")
        print(f"欄位：{df.columns.tolist()}")

    except Exception as e:
        print(f"讀取失敗：{e}")
