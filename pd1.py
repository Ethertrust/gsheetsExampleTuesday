import numpy as np
import pandas as pd


# DataFrame & Series
dfs_dict = pd.read_excel("Data_for_pandas/4 wave p&db.xlsx", sheet_name= ["Performance"], header= 1)
pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 2000)
pd.set_option('display.max_rows', 400)
print(type(dfs_dict))
# print(dfs_dict)
df1 = dfs_dict["Performance"]
print(type(df1))
print(df1)
df2 = pd.read_csv("Data_for_pandas\\Fishing.csv")
print(type(df2))
print(df2)
np_arr = np.load("Data_for_pandas\\arr_pandas.npy", allow_pickle=True)
# print(np_arr, type(np_arr))
#["name","dist","climb","time","timef","type"]
df3 = pd.DataFrame(np_arr)
print(type(df3))
print(df3)
# 1. Стандартная индексация df3[1:-1]
# 2. .loc[]
# 3. .iloc[]
# 1.1 Стандартная индексация df3[1:-1]
print(df3[0:3])
print(df3[0:3][0:1])
print(df3[0])
print(type(df3[0]))
print(df3[0:1])
print(type(df3[0:1]))
# print(df3[0:3, 0:2])
# 2.1 .loc[]
print(df3.loc[0:3, 0:2])
# 3.1 .iloc[]
print(df3.iloc[0:3, 0:2])
b_df = df3.loc[:, 1:2] > 20
print(b_df)
b_s = (df3.loc[:, 1] > 20) | (df3.loc[:, 2] > 2000)
print(b_s)
# 1.2 Стандартная индексация df3[1:-1] с булевыми выборками
print(df3[b_df])
print(df3[b_s])
# 2.2 .loc[]
# print(df3.loc[b_df])
print(df3.loc[b_s, 0:2])
# # 3.2 .iloc[]
# print(df3.iloc[b_df])
# print(df3.iloc[b_s, 0:2])
print("---------- Именованные индексы")
df4 = df3[0:3]
print(df4)
df4.columns = ["name","dist","climb","time","timef","type"]
print(df4)
df4.index = ["third", "first", "second"]
print(df4)
#1.1.2 Стандартная индексация df3[1:-1]
print(df4[0:2])
# print(df4[0])
print(type(df4[0:2]["name"]))
print(df4[0:2]["name"])
# print(type(df4[0:2]))
# print(df4[0:2])
print("-----")
print(type(df4[0:2]["name":]))
print(df4[0:2]["name":])
#2.1.2 .loc[]
# print(df4.loc[0:2])
print(df4.loc["first":,"climb":])
print(df4.loc["first":"second","climb":"timef"])
#2.1.2 .iloc[]
print(df4.iloc[0:2])
print(df4.iloc[0:2, 0:2])
# print(df4.iloc["first":"second","climb":"timef"])

