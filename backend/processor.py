import pandas as pd
import os

def process_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "sample_data.csv")

    df = pd.read_csv(file_path)

    df["processed"] = df["value"] * 2
    print(df)
