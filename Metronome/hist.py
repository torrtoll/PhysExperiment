#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


FILENAME = "data.csv"

# データフレームの作成
df = pd.read_csv(FILENAME, header=None, names=("DataNo", "Time"), index_col="DataNo")
data = (df["Time"] - 1) * 100  # 小数点以下のみ抽出

# 基本統計量の表示
print(data.describe())

# ヒストグラムの描画
fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
ax1.hist(data, range=(30, 80), bins=50, normed=False, color="k", alpha=0.75)
ax1.set_ylim(0, 50)
ax1.set_xlabel("Time [(1.x)s]")
ax1.set_ylabel("Freq")
plt.savefig("Histogram.png", dpi=600)

# フィッティング曲線の算出・描画
param = norm.fit(data)
x = np.linspace(30, 80, 100)
pdf_fitted = norm.pdf(x, loc=param[0], scale=param[1])

fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
ax2.hist(data, range=(30, 80), bins=50, normed=True, histtype="stepfilled", color="k", alpha=0.50)
ax2.plot(x, pdf_fitted, color="k", linewidth=3)
ax2.set_ylim(0, 0.15)
ax2.set_xlabel("Time [(1.x)s]")
ax2.set_ylabel("Freq")

ax2.axvline(x=param[0], color='k', linewidth=1.5, linestyle="--")
ax2.axvline(x=param[0] + param[1], color='k', linewidth=1, linestyle="--")
ax2.axvline(x=param[0] - param[1], color='k', linewidth=1, linestyle="--")
plt.savefig("Fitting.png", dpi=600)
