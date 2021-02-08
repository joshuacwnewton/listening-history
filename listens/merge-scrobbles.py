import pandas as pd    # DataFrame manipulation

path_tsv_2009_2014 = "listens/export-2009-2014/data/scrobbles.tsv"
df_old = pd.read_csv(path_tsv_2009_2014, sep='\t', header=0)
df_old["DateTime"] = pd.to_datetime(df_old['unixtime'], unit='s')
df_old.set_index("DateTime", inplace=True)
df_old.drop(["unixtime", "ISO time", "track mbid", "artist mbid", "uncorrected track name",
             "uncorrected track mbid", "uncorrected artist name", "uncorrected artist mbid", "album mbid",
             "album artist name", "album artist mbid", "application"], axis="columns", inplace=True)

path_csv_2014_2017 = "listens/scrobbles-2014-2017.csv"
df_new = pd.read_csv(path_csv_2014_2017, names=["artist name", "album name", "track name", "DateTime"])
df_new["DateTime"] = pd.to_datetime(df_new["DateTime"])
df_new.set_index("DateTime", inplace=True)

path_csv_2018_2020 = "listens/scrobbles-2018-2020.csv"
df_newest = pd.read_csv(path_csv_2018_2020, names=["artist name", "album name", "track name", "DateTime"])
df_newest["DateTime"] = pd.to_datetime(df_newest["DateTime"])
df_newest.set_index("DateTime", inplace=True)
df_newest.tail()

df_listens = pd.concat([df_old, df_new, df_newest])
df_listens.to_csv("listens/scrobbles-merged-2009-2020.csv")
