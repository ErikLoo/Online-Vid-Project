import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

sylb_list =  [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 2, 4, 0, 0, 0, 0, 1, 2, 4, 0, 0, 0, 0, 4, 5, 3, 5, 5, 2, 4, 0, 5, 5, 2, 6, 1, 0, 5, 5, 5, 3, 6, 2, 4, 5, 4, 5, 3, 6, 0, 0, 0, 4, 2, 2, 3, 5, 5, 0, 0, 5, 3, 5, 5, 5, 4, 1, 4, 4, 0, 2, 5, 5, 6, 1, 5, 1, 0, 5, 5, 2, 5, 4, 1, 2, 5, 5, 1, 3, 4, 1, 0, 0, 1, 5, 3, 4, 6, 3, 1, 5, 3, 3, 4, 6, 0, 0, 4, 4, 3, 2, 3, 3, 5, 0, 5, 3, 1]

tlt_sylb = 319

tlt_num_wrd = 306

sylb_list = np.array(sylb_list)*(306/319)*60

vid_length = 120

sylbs = {"time":np.linspace(0,120,len(sylb_list)),"num_sylb":sylb_list}

df = pd.DataFrame(sylbs)

df["win_5"] = df["num_sylb"].rolling(window=5,min_periods=1).mean().fillna(0)
df["win_10"] = df["num_sylb"].rolling(window=10,min_periods=1).mean().fillna(0)
df["win_15"] = df["num_sylb"].rolling(window=15,min_periods=1).mean().fillna(0)
df["win_20"] = df["num_sylb"].rolling(window=20,min_periods=1).mean().fillna(0)
df["win_25"] = df["num_sylb"].rolling(window=25,min_periods=1).mean().fillna(0)
df["win_30"] = df["num_sylb"].rolling(window=30,min_periods=1).mean().fillna(0)
print(df)

df.plot(x="time",y=["win_5","win_10","win_15","win_20","win_25","win_30"],kind="line")

plt.xlabel('Time (sec)', fontsize=18)
plt.ylabel('Video speed (WPM)', fontsize=18)


plt.show()

