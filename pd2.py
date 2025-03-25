import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 2000)

df1 = pd.read_csv("Data_for_pandas\\Fishing.csv")
print(df1)

# Можно ли сказать, что люди с более низким доходом и выбравшие более дешёвый тип рыбалки, в целом,
# предпочитают один тип рыбалки, а люди с более высоким доходом и более дорогой рыбалкой – другой?

print(df1["income"].max())
# 1. Проверить целостность данных Null - Битых значений нет
# 2. Категоризировать богатых и не богатых
# 3. Категоризировать расходы: разделить их на высокие и остальные
# 3.5
# 4. Сгруппировать и аггрегировать: суммировать, среднее, количество, свой
# 5. Сравнить полученные группы
print(df1.isnull().values.any())
print(df1.sort_values("income", ascending=True))
# print(df1)
print(df1)
print(df1.describe())
print(df1.loc[:, "price":].median())
df1["class"] = pd.cut(df1["income"], 3, labels=["low", "middle", "rich"])
# df2 = pd.DataFrame([[1000],[1000],[1000],[1000],[900]])
# print(df2)
# print(df2.median())
# print(df2.mean())
# print(df1["income"].mean() - df1["income"].median())
# print(df2[0].mean() - df2[0].median())
df1["expenses"] =  pd.cut(df1["price"], 3, labels=["low", "medium", "high"])
rich = df1["class"] == "rich"
not_rich = (df1["class"] == "low") | (df1["class"] == "middle")
not_rich_not_middle = (df1["class"] == "low")
high_exp = df1["expenses"] == "high"
not_high_exp = (df1["expenses"] == "low") | (df1["expenses"] == "medium")
df_rich_high = df1[(rich)&(high_exp)]
df_rich_not_high = df1[(rich)&(not_high_exp)]
df_rich = df1[rich]
df_not_rich = df1[not_rich]

# print(df1.loc[low].describe())
print(df_rich_high.describe())
print(df_rich_not_high)
print(df_rich_high)
# print(df_rich)

def approval_rate(x):
    return x.mean() - x.median()

def first_research(df, title = ""):
    grp = df.groupby("mode")
    print("-------------------------", title)
    print(grp.agg({"price": ["count", "sum", "mean", "median", approval_rate], "income": ["count", "sum", "mean", "median", approval_rate]}))


first_research(df_rich, "Богатые")
first_research(df_not_rich, "Не богатые")
df_not_rich_not_middle = df1[not_rich_not_middle]
first_research(df_not_rich_not_middle, "Низкие доходы")


