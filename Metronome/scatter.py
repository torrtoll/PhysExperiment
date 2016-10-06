#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines
import scipy.stats


FILENAME = "data.csv"


def shift(df):
    # 1行ずらした列をdfに追加する関数
    row_shift = list(df["i"])[1:]
    row_shift.append(None)  # 行数調整
    df["i+1"] = row_shift
    return df


# データフレームの作成
df = pd.read_csv(FILENAME, header=None, names=("DataNo", "i"), index_col="DataNo")
shift(df)

# データの小数点以下を抜き出す
df = (df - 1) * 100
# 100-101,200-201,…回目のデータに意味は無いので(連続していないから)削除する
delete_list = []
for x in range(1, len(list(df["i"])) + 1):
    if x % 100 == 0:
        delete_list.append(x)
df = df.drop(delete_list)
df.to_csv("df.csv")

# 回帰直線と相関係数の算出
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df["i"], df["i+1"])
func = lambda x: x * slope + intercept  # 回帰直線の定義
print("傾き 切片 相関係数:", slope, intercept, r_value)

# 散布図の作成(含回帰直線の描画)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df["i"], df["i+1"], color="k", edgecolors="k", alpha=1)
line = lines.Line2D([30, 80], [func(30), func(80)], linestyle="--",
                    color="k", linewidth=2, alpha=0.50)
ax.add_line(line)
ax.set_xlabel('Time of i [(1.x)s]')
ax.set_ylabel('Time of (i+1) [(1.x)s]')
fig.savefig("Scatter.png", dpi=600)
