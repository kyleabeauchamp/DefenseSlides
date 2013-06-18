import matplotlib.pyplot as plt
import pandas as pd

outdir = "/home/kyleb/src/kyleabeauchamp/personal/defense/figures/"

d = pd.read_csv("./msmbuilder_stats.csv", parse_dates=[[0,1,2]])
x = d.groupby("User").first()["year_month_day"]
x.sort()
x.name = "Time"

y = arange(len(x)) + 1
y = pd.Series(y, index=x)

y.plot()

plt.title("MSMBuilder User Growth")
plt.ylabel("Num. Unique Users")
plt.savefig(outdir+"/msmb_users.png", bbox_inches='tight')
