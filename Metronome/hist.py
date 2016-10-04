#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILENAME = "data.csv"

# データフレームの作成
df = pd.read_csv(FILENAME, header=None, names=("DataNo", "Second"), index_col="DataNo")


# ヒストグラムの描画
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.hist(df["Second"], histtype="step", bins=40)
ax.set_ylim(0, 50)

plt.show()
