import pandas as pd

FILE_PATH = "./runs/GPT-2-345M-50k/mt_metrics.csv"

df = pd.read_csv(FILE_PATH)

print(df.mean())