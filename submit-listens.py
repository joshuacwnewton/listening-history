import numpy as np
import pandas as pd
import pylistenbrainz
from tqdm import tqdm


def convert_to_unix(series):
    if series.name == "DateTime":
        series = pd.to_datetime(series)
        series = (series - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')

    return series


def append_listen(series):
    if series["DateTime"] != '':
        listens.append(
            pylistenbrainz.Listen(
                track_name=series["track name"],
                artist_name=series["artist name"],
                release_name=series["album name"],
                listened_at=int(series["DateTime"])
            )
        )

    return series  # Don't change the actual dataframe


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


path_csv_2009_2020 = "listens/scrobbles-merged-2009-2020.csv"
df_listens = pd.read_csv(path_csv_2009_2020)

print("Converting DateTime to UNIX time...")
df_listens = df_listens.apply(convert_to_unix)

print("Replacing NANs...")
df_listens = df_listens.replace(np.nan, '', regex=True)

print("Converting to list of listens...")
listens = []
df_listens.apply(append_listen, axis=1)

print("Submitting listens...")
client = pylistenbrainz.ListenBrainz()
client.set_auth_token()

# Submit in smaller chunks, because trying to submit all 70000 results in HTTP 504 Gateway Timeout
for sublist in tqdm(chunks(listens, 100)):
    client.submit_multiple_listens(sublist)
