import pandas as pd

df = pd.read_excel(r"/home/konam/Downloads/budget_1920.xls")

print("The stats of the datset are",df.describe())
