import pandas as pd
import pathlib

p_old = list(pathlib.Path("old_data").glob("*.csv"))[0]
p_new = pathlib.Path("test_data/data.csv")

df = pd.read_csv(p_old)
df["DateTime"] = pd.to_datetime(df["Time"])
del df["Time"]
for c in ["User", "Name", "Path"]:
    df[c] = df[c].str.strip()
df["Name"] = df["Name"].str.split(".", expand=True)[0]
df.to_csv(p_new)
#df.head()