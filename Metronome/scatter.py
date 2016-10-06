#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


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

# 散布図の作成
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df["i"], df["i+1"], c="k", edgecolors="k", alpha=1)
ax.set_xlabel('Time of i [(1.x)s]')
ax.set_ylabel('Time of (i+1) [(1.x)s]')
fig.savefig("Scatter.png", dpi=600)
