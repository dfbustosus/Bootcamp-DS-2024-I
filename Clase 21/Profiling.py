from ydata_profiling import ProfileReport

import pandas as pd

df = pd.read_csv("women_track_records.csv")

profile = ProfileReport(df)

profile.to_file("report.html")