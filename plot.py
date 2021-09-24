import pandas as pd
import matplotlib.pyplot as plt


def satvb(btckvb_list):
    return [float(f) * 10 ** 8 / 10 ** 3 for f in btckvb_list]


columns = [
    "block",
    "2 blocks estimate",
    "4 blocks estimate",
    "8 blocks estimate",
    "32 blocks estimate",
    "144 blocks estimate",
]
df_master = pd.read_csv("fee_est_master.csv", names=columns)
df_rbf = pd.read_csv("fee_est_rbf.csv", names=columns)

targets = columns[1:]
fig, axes = plt.subplots(len(targets))

for i, target in enumerate(targets):
    axes[i].plot(
        df_master["block"], satvb(df_master[target]), color="red", label="master"
    )
    axes[i].plot(df_rbf["block"], satvb(df_rbf[target]), color="blue", label="rbf")
    axes[i].set_title(target)
    axes[i].legend(loc="upper right")

plt.show()
